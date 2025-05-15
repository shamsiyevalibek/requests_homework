"""
Task 2: Create a Function with Error Handling

Goal:
- Create a function that includes error handling for GET requests.

Function requirements:
- Name: safe_get_post(post_id)
- Makes a GET request to https://jsonplaceholder.typicode.com/posts/{post_id}
- Checks the response status code
- If it's not 200, returns a dictionary with {"success": False, "message": "Failed to get data"}
- Otherwise, returns {"success": True, "data": post_data}

Expected Output (Success):
{
  "success": True,
  "data": {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto"
  }
}

Expected Output (Failure):
{
  "success": False,
  "message": "Failed to get data"
}

Your implementation below:
"""

# Your implementation here
import requests  

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
print(safe_get_post(9999))