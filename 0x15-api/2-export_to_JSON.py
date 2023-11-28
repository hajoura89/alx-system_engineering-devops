#!/usr/bin/python3
"""Export to JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    usr_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(usr_id)).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"userId": usr_id}).json()

    with open("{}.json".format(usr_id), "w") as jsonfile:
        json.dump({usr_id: [{
                "task": d.get("title"),
                "completed": d.get("completed"),
                "username": username
            } for d in todo]}, jsonfile)
