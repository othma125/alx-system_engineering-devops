#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API, parses the
title of all hot articles, and prints a sorted count of given keywords"""
from requests import get


def count_words(subreddit, word_list, after="", word_dict={}):
    """Returns the top ten hot words for a given subreddit"""
    if after == "":
        new_word_list = []
        for word in word_list:
            lower = word.lower()
            if lower not in new_word_list:
                new_word_list.append(word.lower())
        word_list = new_word_list
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "My-User-Agent"}
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        for child in data.get("children"):
            text_list = [txt.lower() for txt
                         in child.get("data").get("title").split()]
            for word in text_list:
                if word in word_list:
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
        after = data.get("after")
        if after:
            count_words(subreddit, word_list, after, word_dict)
            return
        for word in word_dict:
            print(f"{word}: {word_dict[word]}")
