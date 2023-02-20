import re
import pandas as pd

with open('tweets.txt', 'r') as f:
    tweets = f.readlines()

racial_slurs_df = pd.read_csv("racial_slurs.csv")
racial_slurs = set(racial_slurs_df["word"].lower())


def is_racial_slur(word):
    return word.lower() in racial_slurs


for i, tweet in enumerate(tweets, start=1):
    words = tweet.strip().split()
    profanity_count = sum(is_racial_slur(word) for word in words)
    if profanity_count == 0:
        pass
    else:
        print(f"Detected : Tweet {i} -> Profanity Score : {profanity_count}")
