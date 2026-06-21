import re

def extract_keywords(text):

    stop_words = [
    "is","am","are","the","a","an",
    "of","in","on","at","for","to",
    "or","not","was","were","do","does"
]

    words = text.lower().split()

    keywords = []

    for word in words:
        if word not in stop_words:
            keywords.append(word)

    return " ".join(keywords)