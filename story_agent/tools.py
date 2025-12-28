# Contains:
# functions to fetch stories
# validation
# error handling
# API calls (Reddit, DB, etc.)
reddit = praw.Reddit(client_id ='my client id', 
	client_secret ='my client secret', 
	user_agent ='my user agent', 
	username ='my username', 
	password ='my password') 
import requests
def fetch_reddit_story(subreddit, sort="top", time_filter="day", min_upvotes=None, allow_nsfw=False):
    url = f"https://www.reddit.com/r/{subreddit}/{sort}.json"
    params = {"t": time_filter, "limit": 10}
    headers = {"User-Agent": "short-gen/0.1 (+your email)"}
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=5)
        resp.raise_for_status()
        data = resp.json()["data"]["children"]
        if not data:
            return {"error": "no posts", "title": None, "body": None, "permalink": None,
                    "author": None, "id": None, "created_utc": None, "nsfw": None}
        for item in data:
            post = item["data"]
            if (not allow_nsfw and post.get("over_18")) or (min_upvotes and post["ups"] < min_upvotes):
                continue
            return {
                "title": post["title"],
                "body": post.get("selftext", "") or post.get("url", ""),
                "permalink": "https://www.reddit.com" + post["permalink"],
                "author": post.get("author"),
                "id": post.get("id"),
                "created_utc": int(post.get("created_utc", 0)),
                "nsfw": bool(post.get("over_18")),
                "error": None,
            }
        return {"error": "no post met filters", "title": None, "body": None, "permalink": None,
                "author": None, "id": None, "created_utc": None, "nsfw": None}
    except Exception as exc:
        return {"error": str(exc), "title": None, "body": None, "permalink": None,
                "author": None, "id": None, "created_utc": None, "nsfw": None}
