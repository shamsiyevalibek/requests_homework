"""
Task 5: Create a Utility Module

Goal:
- Organize all your request functions into a reusable module.

Module requirements:
- Filename: api_client.py
- Contains all previous functions:
  - get_post_data(post_id)
  - safe_get_post(post_id)
  - create_post(title, body, user_id)
  - get_comments_by_post(post_id, limit=3)
- All functions should be properly documented with docstrings
- The module should handle imports appropriately

Your implementation below:
"""

# Your implementation here
import requests

def get_post_data(post_id):

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "title": data["title"],
            "body": data["body"]
        }
    else:
        return {"error": "Post not found"}


def safe_get_post(post_id):

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)

    if response.status_code == 200:
        post_data = response.json()
        return {
            "success": True,
            "data": post_data
        }
    else:
        return {
            "success": False,
            "message": "Failed to get data"
        }


def create_post(title, body, user_id):

    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(url, json=data)
    return response.json()


def get_comments_by_post(post_id, limit=3):
  
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {"postId": post_id}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        comments = response.json()
        return [
            {"name": c["name"], "email": c["email"]}
            for c in comments[:limit]
        ]
    else:
        return []
from api_client import get_post_data, create_post

print(get_post_data(1))

