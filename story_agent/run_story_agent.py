# This is how:
# you test the agent
# other agents call it later
# pipelines integrate it
# story_agent/run_story_agent.py
from story_agent.state import AgentState, UserIntent  # adjust import paths if needed
from story_agent.agent_loop import run_agent_loop     # you’ll define this
# from story_agent.tools import init_tools             # if you need to prep tool clients (e.g., Reddit)

def main():
    # TODO: replace this with your real input source (CLI args, function params, etc.)
    subreddit = "AskReddit"
    sort = "top"
    time_filter = "day"
    min_upvotes = None

    # 1) Build user intent and initial state
    intent = UserIntent(
        subreddit=subreddit,
        sort=sort,
        time_filter=time_filter,
        min_upvotes=min_upvotes,
        allow_nsfw=False,
    )
    state = AgentState(user_intent=intent)

    # 2) (Optional) set up any tool clients/config
    # tools = init_tools()

    # 3) Run the agent loop until it stops
    final_state = run_agent_loop(state)  # pass tools if your loop expects them

    # 4) Produce output (for now, just print)
    if final_state.status.outcome == "success" and final_state.fetched_story:
        print(final_state.fetched_story.title)
        print(final_state.fetched_story.body)
        print(final_state.fetched_story.url)
    else:
        print("No story retrieved:", final_state.status.outcome)

if __name__ == "__main__":
    main()
