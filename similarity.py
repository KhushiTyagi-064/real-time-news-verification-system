from sentence_transformers import SentenceTransformer
from sentence_transformers import util

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_similarity(text1, text2):

    emb1 = model.encode(text1)
    emb2 = model.encode(text2)

    score = util.cos_sim(emb1, emb2)

    return float(score[0][0])