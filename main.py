import requests
from send_email import send_email

api_key = "3b698c746dfe495d87aab433fb0fe9e4"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2023-04-30&sortBy" \
      "=publishedAt&apiKey=3b698c746dfe495d87aab433fb0fe9e4"

# make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)