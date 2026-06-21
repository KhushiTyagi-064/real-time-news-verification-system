from text import search_news
from similarity import get_similarity
from keyword_extract import extract_keywords
from credibility import get_credibility

user_news = input("Enter News Headline: ")

search_query = extract_keywords(user_news)

print("\nSearching News...")
print("Keywords:", search_query)

articles = search_news(search_query)

if len(articles) == 0:

    print("No related news found.")

else:

    best_score = 0
    best_article = ""
    best_source = ""

    for article in articles:

        title = article["title"]
        source = article["source"]

        score = get_similarity(
            user_news,
            title
        )

        print("\nTitle:", title)
        print("Source:", source)
        print("Similarity:", round(score, 2))

        if score > best_score:

            best_score = score
            best_article = title
            best_source = source

    credibility = get_credibility(best_source)

    print("\n========================")
    print("BEST MATCH")
    print("========================")

    print("Title:", best_article)
    print("Source:", best_source)
    print("Credibility:", credibility, "%")
    print("Similarity Score:", round(best_score, 2))

    if best_score >= 0.75:

        print("\nRESULT: LIKELY REAL")

    elif best_score >= 0.50:

        print("\nRESULT: NEEDS VERIFICATION")

    else:

        print("\nRESULT: LIKELY FAKE")