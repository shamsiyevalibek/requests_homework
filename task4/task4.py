"""
Task 4: Create a Function Using Query Parameters

Goal:
- Create a function that sends a GET request with URL parameters.

Function requirements:
- Name: get_comments_by_post(post_id, limit=3)
- Makes a GET request to https://jsonplaceholder.typicode.com/comments with the query parameter postId={post_id}
- Returns a list of dictionaries, each containing 'name' and 'email' from the first {limit} comments

Expected Output (post_id=1, limit=3):
[
  {
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz"
  },
  {
    "name": "quo vero reiciendis velit similique earum",
    "email": "Jayne_Kuhic@sydney.com"
  },
  {
    "name": "odio adipisci rerum aut animi",
    "email": "Nikita@garfield.biz"
  }
]

Your implementation below:
"""

# Your implementation here
import requests

def get_comments_by_post(post_id, limit=3):
    url = "https://jsonplaceholder.typicode.com/comments"

    params = {
        "postId": post_id   
    }

    response = requests.get(url, params=params)  

    if response.status_code == 200:
        comments = response.json() 
        
        result = []
        for comment in comments[:limit]:  
            result.append({
                "name": comment["name"],
                "email": comment["email"]
            })
        
        return result

    else:
        return [] 
print(get_comments_by_post(9,limit=3))
