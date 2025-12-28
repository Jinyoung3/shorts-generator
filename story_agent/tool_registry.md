# Tool Registry

- name: fetch_reddit_story
  purpose: Retrieve a single post from a subreddit based on filters.
  inputs:
    - subreddit (string, required, lowercase, allowed list)
    - sort (enum: hot|top|new, default=top)
    - time_filter (enum: day|week|month, default=day when sort=top)
    - min_upvotes (int, optional)
    - allow_nsfw (bool, default=false; must be false)
  outputs:
    - title (string)
    - body (string)
    - permalink (url)
    - author (string)
    - created_utc (int)
    - nsfw (bool)
    - error (string|null)
  constraints:
    - Reject nsfw posts.
    - Enforce min_upvotes if provided; retry up to 2 times then return error.
    - Timeout 5s per call.

- name: request_new_story
  purpose: Ask user to request another source/story.
  inputs:
    - reason (string, required)
    - requested_source (string, required)
  outputs:
    - message (string)
  constraints:
    - No network calls; just produce guidance.
