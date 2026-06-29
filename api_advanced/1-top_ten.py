#!/usr/bin/python3
"""Module that queries the Reddit API and prints top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints None if subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:reddit.api.project:v1.0.0 (by /u/reddit_api_user)"
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
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
