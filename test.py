import praw
import sqlite3

user_agent = "script:theriddler:v0.0.1 (by u/kpuc1997)"

with open("client.id") as f:
    client_id = f.read()

with open("client.secret") as f:
    SECRET = f.read()

reddit = praw.Reddit(client_id=client_id,
                     client_secret=SECRET,
                     user_agent=user_agent)

with open("riddles.txt", "a", encoding="utf8") as f:
    for submission in reddit.subreddit("riddles").hot(limit=100):
        f.write(submission.selftext)

