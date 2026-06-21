from similarity import get_similarity

news1 = "NASA plans a mission to Mars"

news2 = "NASA announces Mars mission"

score = get_similarity(news1, news2)

print("Similarity Score:", score)