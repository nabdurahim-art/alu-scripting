#!/usr/bin/python3
"""Module that queries the Reddit API and prints top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced-project"}
    params = {"limit": 10, "raw_json": 1}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if response.status_code != 200:
        print(None)
        return
    results = response.json().get("data", {}).get("children", [])
    if not results:
        print(None)
        return
    for post in results:
        print(post.get("data", {}).get("title"))
