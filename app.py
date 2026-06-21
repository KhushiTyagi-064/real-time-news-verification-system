import streamlit as st

from text import search_news
from similarity import get_similarity
from credibility import get_credibility
from keyword_extract import extract_keywords


st.set_page_config(
    page_title="News Verification System",
    page_icon="📰"
)

st.title("📰 Real-Time News Verification System Using NLP")

st.write(
    "Check whether a news claim is supported by trusted news sources."
)

user_news = st.text_area(
    "Enter News Headline or Claim"
)

if st.button("Analyze News"):

    if user_news.strip() == "":
        st.warning("Please enter a news headline.")
        st.stop()

    keywords = extract_keywords(user_news)

    st.info(f"Keywords Used: {keywords}")

    articles = search_news(keywords)

    if len(articles) == 0:

        st.warning(
            "No recent news articles found. Try a complete news headline."
        )

    else:

        best_score = 0
        best_article = ""
        best_source = ""
        best_url = ""

        for article in articles:

            score = get_similarity(
        user_news,
        article["title"]
    )

            if score < 0.20:
                continue

            if score > best_score:

                best_score = score
                best_article = article["title"]
                best_source = article["source"]
                best_url = article["url"]

        similarity_percentage = round(best_score * 100, 2)

        credibility_score = get_credibility(best_source)

        st.subheader("Best Matching Article")

        st.success(best_article)

        st.write("Source:", best_source)

        st.write("Article Link:")
        st.write(best_url)

        st.metric(
            "Similarity Score",
            f"{similarity_percentage}%"
        )

        st.metric(
            "Source Credibility",
            f"{credibility_score}/100"
        )

        if best_score >= 0.70:

            st.success(
                "✅ Likely Real"
            )

        elif best_score >= 0.40:

            st.warning(
                "⚠️ Needs Verification"
            )

        else:

            st.error(
                "❌ Likely Fake"
            )

        st.subheader("Related Articles")

        for article in articles:

            st.write("•", article["title"])