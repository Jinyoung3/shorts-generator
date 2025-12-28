from dataclasses import dataclass, field
from typing import Optional

@dataclass
class UserIntent:
    subreddit: str
    sort: str = "top"         # hot|top|new
    time_filter: str = "day"  # day|week|month when sort=top
    min_upvotes: Optional[int] = None
    allow_nsfw: bool = False

@dataclass
class Attempt:
    retries: int = 0
    last_error: Optional[str] = None

@dataclass
class Story:
    id: str
    title: str
    body: str
    url: str
    author: str
    created_utc: int
    nsfw: bool

@dataclass
class Status:
    done: bool = False
    outcome: Optional[str] = None  # success|error|needs_new_story

@dataclass
class AgentState:
    user_intent: UserIntent
    attempt: Attempt = field(default_factory=Attempt)
    fetched_story: Optional[Story] = None
    status: Status = field(default_factory=Status)
