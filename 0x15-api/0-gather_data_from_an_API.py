#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

# from pprint import pprint
import requests
import sys

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + f"/user/{sys.argv[1]}/todos"
    name_url = main_url + f"/users/{sys.argv[1]}"
    todo_result = requests.get(todo_url).json()
    name_result = requests.get(name_url).json()
    # pprint(todo_result)
    # pprint(name_result)
    n = len([todo for todo in todo_result
             if todo.get("completed")])
    print(f"Employee {name_result.get('name')} "
          f"is done with tasks({n}/{len(todo_result)}):")
    for todo in todo_result:
        if todo.get("completed"):
            print(f"\t {todo.get('title')}")
