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
        "User-Agent": "Mozilla/5.0 (Linux; ALU Project) python3-requests"
    }
    params = {"limit": 10}
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
    except requests.exceptions.RequestException:
        print(None)
        return

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
