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
    question = {
        "question": "個人情報保護の法制度に関する以下のアからエまでの記述のうち、誤っているものはどれか。",
        "candidates": [
            {
                "text": "OECD（経済協力開発機構）の理事会勧告、いわゆるOECD8原則は、先進国における個人情報保護法制のスタンダードとなり、日本の個人情報保護法にも取り入れられている。",
                "correct": True,
                "description": "個人情報保護に関する法制度は、１９７０年代から個人情報のコンピュータ処理の広まりにともない、米国やドイツ、フランスなどの先進国で整備されるようになった。"
            },
            {
                "text": "EU（欧州連合）が1995年に制定した「個人データ保護指令」は、EU域外の第三国への個人情報の移転の制限についても定められていたため、日本もその対応が求められ個人情報保護法制の整備が急務となった。",
                "correct": False,
                "description": "個人情報保護に関する法制度は、１９７０年代から個人情報のコンピュータ処理の広まりにともない、米国やドイツ、フランスなどの先進国で整備されるようになった。"
            },
            {
                "text": "情報通信技術の発展により個人情報保護の必要性が高まり、OECD8原則が示されたことが、個人情報保護法の制定の契機となったといえる。",
                "correct": False,
                "description": "個人情報保護に関する法制度は、１９７０年代から個人情報のコンピュータ処理の広まりにともない、米国やドイツ、フランスなどの先進国で整備されるようになった。"
            },
            {
                "text": "日本では個人情報保護法の制定により個人情報の保護が図られることになり、これを契機として住民基本台帳ネットワーク（いわゆる住基ネット）の導入が検討されることになった。",
                "correct": False,
                "description": "個人情報保護に関する法制度は、１９７０年代から個人情報のコンピュータ処理の広まりにともない、米国やドイツ、フランスなどの先進国で整備されるようになった。"
            }
        ]
    }

    question = random.choice(questions)
    random.shuffle(question["candidates"])
    return jsonify(question), 200


if __name__ == "__main__":
    app.run(debug=True)
