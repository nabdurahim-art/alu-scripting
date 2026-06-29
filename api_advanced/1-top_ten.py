#!/usr/bin/python3
"""Module that queries Reddit API and prints top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0 by /u/myuser"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
