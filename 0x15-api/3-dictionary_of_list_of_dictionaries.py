#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            s.get("id"): [{
                "task": d.get("title"),
                "completed": d.get("completed"),
                "username": s.get("username")
            } for d in requests.get(url + "todos",
                                    params={"userId": s.get("id")}).json()]
            for s in users}, jsonfile)
