def get_credibility(source):

    trusted_sources = {
        "BBC News": 95,
        "Reuters": 98,
        "CNN": 90,
        "The Hindu": 90,
        "Times of India": 85
    }

    return trusted_sources.get(source, 60)