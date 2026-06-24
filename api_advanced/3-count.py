#!/usr/bin/python3
"""Module that recursively queries Reddit API and counts keyword occurrences"""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """Prints sorted count of keywords found in hot article titles"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {"User-Agent": "MyBot/1.0 by /u/myuser"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    posts = data.get("children", [])
    if not posts:
        return
    for word in word_list:
        w = word.lower()
        if w not in counts:
            counts[w] = 0
    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            w = word.lower()
            counts[w] += title.count(w)
    after = data.get("after")
    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
        return
    return count_words(subreddit, word_list, counts, after)
