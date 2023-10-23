#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

from sys import argv
from requests import get

# from pprint import pprint

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + f"/user/{argv[1]}/todos"
    name_url = main_url + f"/users/{argv[1]}"
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()
    # pprint(todo_result)
    # pprint(name_result)
    n = len([todo for todo in todo_result
             if todo.get("completed")])
    print(f"Employee {name_result.get('name')} "
          f"is done with tasks({n}/{len(todo_result)}):")
    for todo in todo_result:
        if todo.get("completed"):
            print(f"\t {todo.get('title')}")
