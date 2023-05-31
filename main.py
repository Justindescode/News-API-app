import requests
from send_email import send_email

topic = "tesla"

api_key = "3b698c746dfe495d87aab433fb0fe9e4"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=" \
      "2023-04-30&" \
      "sortBy=publishedAt&" \
      "apiKey=3b698c746dfe495d87aab433fb0fe9e4"


# make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] \
               + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
