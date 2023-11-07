#!/usr/bin/python3
"""Returns the top ten hot posts for a given subreddit"""
from requests import get


def top_ten(subreddit):
    """Returns the top ten hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        for child in data.get("children")[:10]:
            print(child.get("data").get("title"))
    else:
        print("None")
