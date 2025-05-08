📘 Python requests Homework
🔧 Prerequisites
Make sure you have the requests library installed:

bash
Copy
Edit
pip install requests

📝 Task 1: Create a GET Request Function
Goal: Create a function to get data from a public API.

✅ Instructions:

Create a function `get_post_data(post_id)` that:
- Makes a GET request to https://jsonplaceholder.typicode.com/posts/{post_id}
- Returns a dictionary with the title and body of the post

Test your function with post_id = 1.

📊 Expected Output:
```
{
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto"
}
```

📝 Task 2: Create a Function with Error Handling
Goal: Create a function that includes error handling for GET requests.

✅ Instructions:

Create a function `safe_get_post(post_id)` that:
- Makes a GET request to https://jsonplaceholder.typicode.com/posts/{post_id}
- Checks the response status code
- If it's not 200, returns a dictionary with {"success": False, "message": "Failed to get data"}
- Otherwise, returns {"success": True, "data": post_data}

Test your function with valid and invalid post IDs.

📊 Expected Output (Success):
```
{
  "success": True,
  "data": {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto"
  }
}
```

📊 Expected Output (Failure):
```
{
  "success": False,
  "message": "Failed to get data"
}
```

📝 Task 3: Create a POST Request Function
Goal: Create a function to send data to a server using POST.

✅ Instructions:

Create a function `create_post(title, body, user_id)` that:
- Sends a POST request to https://jsonplaceholder.typicode.com/posts
- Includes the title, body, and userId in the request JSON data
- Returns the server's response data

Test your function with: create_post("My Homework", "I am learning requests!", 1)

📊 Expected Output:
```
{
  "title": "My Homework",
  "body": "I am learning requests!",
  "userId": 1,
  "id": 101
}
```

📝 Task 4: Create a Function Using Query Parameters
Goal: Create a function that sends a GET request with URL parameters.

✅ Instructions:

Create a function `get_comments_by_post(post_id, limit=3)` that:
- Makes a GET request to https://jsonplaceholder.typicode.com/comments with the query parameter postId={post_id}
- Returns a list of dictionaries, each containing 'name' and 'email' from the first {limit} comments

Test your function with: get_comments_by_post(1, 3)

📊 Expected Output:
```
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
```

📝 Task 5: Create a Utility Module
Goal: Organize all your request functions into a reusable module.

✅ Instructions:

Create a file named `api_client.py` that contains all your previous functions:
- get_post_data(post_id)
- safe_get_post(post_id)
- create_post(title, body, user_id)
- get_comments_by_post(post_id, limit=3)

Create a simple main.py file that imports your module and demonstrates each function.

📊 Expected Output (when running main.py):
```
Task 1 - Get Post:
{title: "sunt aut facere...", body: "quia et suscipit..."}

Task 2 - Safe Get (Success):
{"success": true, "data": {...}}

Task 2 - Safe Get (Failure):
{"success": false, "message": "Failed to get data"}

Task 3 - Create Post:
{title: "My Homework", body: "I am learning requests!", userId: 1, id: 101}

Task 4 - Get Comments:
[{name: "id labore ex et quam laborum", email: "Eliseo@gardner.biz"}, ...]
```

