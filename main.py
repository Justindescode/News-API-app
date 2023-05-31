import requests

api_key = "3b698c746dfe495d87aab433fb0fe9e4"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2023-04-30&sortBy" \
      "=publishedAt&apiKey=3b698c746dfe495d87aab433fb0fe9e4"

# make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and descriptionn
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
