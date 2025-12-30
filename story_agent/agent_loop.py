
# Here is the correct mental model:
# Load agent prompt
# Load current stat
# Show agent the available tools
# Ask agent: “What should we do next?”
# If agent says “use tool X”:
# execute tool X
# update state
# If agent outputs a final decision:
# store decision
# stop loop

from tools import fetch_reddit_story
import { OpenRouter } from '@openrouter/sdk';
import requests
import json

# First API call with reasoning
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "xiaomi/mimo-v2-flash:free",
    "messages": [
        {
          "role": "user",
          "content": "How many r's are in the word 'strawberry'?"
        }
      ],
    "reasoning": {"enabled": True}
  })
)

# Extract the assistant message with reasoning_details
response = response.json()
response = response['choices'][0]['message']

# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
  {
    "role": "assistant",
    "content": response.get('content'),
    "reasoning_details": response.get('reasoning_details')  # Pass back unmodified
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  data=json.dumps({
    "model": "xiaomi/mimo-v2-flash:free",
    "messages": messages,  # Includes preserved reasoning_details
    "reasoning": {"enabled": True}
  })
)

def load_prompt():
    with open("story_agent/prompt_template.md", "r", encoding="utf-8") as f:
        return f.read()
def llm_call():

def agent():
	prompt=load_prompt()
	result = fetch_reddit_story(
		state.user_intent.subreddit,
		sort=state.user_intent.sort,
		time_filter=state.user_intent.time_filter,
		min_upvotes=state.user_intent.min_upvotes,
		allow_nsfw=state.user_intent.allow_nsfw,
		use_stube=True
	)
	if result["error"]:
		state.status.outcome = "error"
		state.status.done=True
		state.attempt.last_error = result["error"]
		return state 
	state.fetched_story=result
	state.status.outcome="success"
	state.status.done=True
	return state 
		