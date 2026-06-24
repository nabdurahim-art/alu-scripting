#!/usr/bin/python3
"""Module that queries Reddit API and prints top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Custom User-Agent to avoid getting 429 Too Many Requests errors from Reddit
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    params = {"limit": 10}
    
    try:
        # allow_redirects=False handles invalid subreddits that redirect to search results
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        
        # If redirect happens (3xx) or error (4xx/5xx), print None and exit
        if response.status_code != 200:
            print(None)
            return
        
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        # If the subreddit is empty or invalid data structure returned
        if not posts:
            print(None)
            return
            
        # Explicitly slice the first 10 elements to satisfy the exact count requirement
        for post in posts[:10]:
            print(post.get("data", {}).get("title"))
            
    except Exception:
        print(None)
