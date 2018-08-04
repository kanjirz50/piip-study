import csv
import random

from flask import Flask, render_template, jsonify, request


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/question")
def question():
    question = random.choice(questions)
    random.shuffle(question["candidates"])

    return jsonify(question), 200


if __name__ == "__main__":
    app.run(debug=True)
