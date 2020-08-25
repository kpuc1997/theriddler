import praw
import sqlite3
import time

num_riddles = 1000

user_agent = "script:theriddler:v0.0.1 (by u/kpuc1997)"

with open("client.id") as f:
    client_id = f.read()

with open("client.secret") as f:
    SECRET = f.read()

reddit = praw.Reddit(client_id=client_id,
                     client_secret=SECRET,
                     user_agent=user_agent)

with open("riddles.txt", "w") as f:
    f.write("")

actual_riddles = 0

start = time.perf_counter()
with open("riddles.txt", "a", encoding="utf8") as f:
    for submission in reddit.subreddit("riddles").new(limit=num_riddles):
        f.write("<|startoftext|>\n")
        f.write(submission.selftext)
        f.write("\n<|endoftext|>\n")
        actual_riddles += 1
runtime = time.perf_counter() - start

print(f"{actual_riddles} riddles collected in {runtime:0.2f} seconds")