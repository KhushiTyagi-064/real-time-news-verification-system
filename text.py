import requests

API_KEY = "e4d6611ea890446cbb01ebbfc5cff097"


def search_news(query):

    url = (
        f"https://newsapi.org/v2/everything?"
        f'q="{query}"&language=en&sortBy=publishedAt&apiKey={API_KEY}'
    )

    response = requests.get(url)

    data = response.json()

    articles = []

    if "articles" in data:

        for article in data["articles"][:5]:

            articles.append({
                "title": article["title"],
                "source": article["source"]["name"],
                "url": article["url"]
            })

    return articles