import csv
import re

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def ngram(words, n):
    return list(zip(*(words[i:] for i in range(n))))


def sentences_to_docs(sentences):
    docs = []
    for sentence in sentences:
        ngrams = ["".join(n) for n in ngram(re.sub(r" \n\t\r", "", sentence), 2)]
        docs.append(" ".join(ngrams))
    return docs


def get_vector(questions):
    sentences = []
    for question in questions:
        sentences.append("".join([candidate["text"] for candidate in question["candidates"]]))

    docs = sentences_to_docs(sentences)

    vectorizer = CountVectorizer()
    vec = vectorizer.fit_transform(docs)
    return vec


def get_similar_question_idx(vector, idx):
    cos_sims = cosine_similarity(vector, vector)
    return cos_sims[idx].argsort()[-2]


def read_question():
    with open("./個人情報保護士問題と解説.tsv", "r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin, delimiter="\t")
        questions = []
        for row in reader:
            question = {
                "question": row["問題"],
                "candidates": [
                    {
                        "text": row["選択肢1"],
                        "correct": row["答え"] == "1",
                        "description": row["解説1"],
                    },
                    {
                        "text": row["選択肢2"],
                        "correct": row["答え"] == "2",
                        "description": row["解説2"],
                    },
                    {
                        "text": row["選択肢3"],
                        "correct": row["答え"] == "3",
                        "description": row["解説3"],
                    },
                    {
                        "text": row["選択肢4"],
                        "correct": row["答え"] == "4",
                        "description": row["解説4"],
                    },
                ]
            }
            questions.append(question)
    return questions