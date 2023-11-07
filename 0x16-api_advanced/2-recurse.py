#!/usr/bin/python3
"""Returns the top ten hot posts for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns the top ten hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        for child in data.get("children"):
            hot_list.append(child.get("data").get("title"))
        after = data.get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
