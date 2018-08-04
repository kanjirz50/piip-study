import random

from flask import Flask, render_template, jsonify, request

from utils import read_question, get_vector, get_similar_question_idx


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

questions = read_question()
vec = get_vector(questions)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/question")
def question():
    similar_question_index = request.args.get("sim_q_idx", "")

    if similar_question_index == "":
        question = random.choice(questions)
    else:
        question = get_similar_question_idx(vec, similar_question_index)

    random.shuffle(question["candidates"])
    return jsonify(question), 200


if __name__ == "__main__":
    app.run(debug=True)
