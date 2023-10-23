#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to CSV"""

from csv import DictWriter, QUOTE_ALL
import requests
import sys

if __name__ == "__main__":
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + f"/user/{sys.argv[1]}/todos"
    name_url = main_url + f"/users/{sys.argv[1]}"
    todo_result = requests.get(todo_url).json()
    name_result = requests.get(name_url).json()
    todo_list = []
    for todo in todo_result:
        my_dict = {"user_ID": sys.argv[1],
                   "username": name_result.get("username"),
                   "completed": todo.get('completed'),
                   "task": todo.get("title")}
        todo_list.append(my_dict)
    with open(f"{sys.argv[1]}.csv", 'w', newline='') as f:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(todo_list)
