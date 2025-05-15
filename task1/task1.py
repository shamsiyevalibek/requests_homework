"""
Task 1: Create a GET Request Function

Goal:
- Create a function to get data from a public API.

Function requirements:
- Name: get_post_data(post_id)
- Makes a GET request to https://jsonplaceholder.typicode.com/posts/{post_id}
- Returns a dictionary with the title and body of the post

Expected Output Example (post_id=1):
{
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto"
}

Your implementation below:
"""

# Your implementation here
import requests  # 1. HTTP so‘rovlar uchun kutubxona

def get_post_data(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"  # 2. API manzilini tayyorlaymiz
    response = requests.get(url)  # 3. GET so‘rovini yuboramiz

    if response.status_code == 200:  # 4. So‘rov muvaffaqiyatli bo‘lsa (status 200 bo‘lsa)
        data = response.json()  # 5. JSON formatidagi javobni dictionary'ga aylantiramiz
        return {
            "title": data["title"],  # 6. faqat kerakli qismlarni ajratamiz
            "body": data["body"]
        }
    else:
        return {"error": "Post not found"}  # 7. xatolik bo‘lsa shunday javob qaytariladi
print(get_post_data(1))
