#!/usr/bin/python3
"""Module that queries the Reddit API and prints top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:myredditapp:v1.2.3 (by /u/ALU_student)"
    }
    params = {"limit": 10}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if response.status_code != 200:
        print(None)
        return
    results = response.json()
    posts = results.get("data", {}).get("children", [])
    if not posts:
        print(None)
        return
    for post in posts:
        print(post.get("data", {}).get("title"))
