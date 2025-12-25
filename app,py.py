from flask import Flask, request, render_template
import random

app = Flask(__name__)

answers = {
    "범인": [
        "범인과 관련된 단서가 여러 개 있습니다. 상황을 정리하고 접근해보세요.",
        "누군가 행동과 정보를 활용했을 수 있습니다. 단서를 다시 확인해보세요."
    ],
    "동기": [
        "동기와 관련된 단서들을 다시 살펴보세요. 개인적 경험과 사회적 맥락이 중요합니다.",
        "행동 뒤에 숨은 이유가 무엇인지 생각해보세요."
    ],
    "방법": [
        "범행 방법은 직업적 지식과 환경을 활용했을 가능성이 있습니다.",
        "행동 방식과 장소 선택에서 단서가 있을 수 있습니다."
    ],
    "시간": [
        "범행 시간대와 환경이 중요합니다. 관련 단서를 떠올려보세요.",
        "퇴근 시간 직전이라는 시점이 의도적으로 선택되었을 수 있습니다."
    ],
    "장소": [
        "장소와 구조 관련 단서를 확인하세요. 내부 구조와 취약점을 참고하면 도움이 됩니다."
    ]
}

hints = [
    "힌트1: 사건 현장과 관련된 정보를 다시 떠올려 보세요.",
    "힌트2: 범행과 관련된 인물들의 배경을 연결해보세요."
]

hint_count = 0
MAX_HINT = 2

@app.route("/", methods=["GET", "POST"])
def index():
    global hint_count
    response = ""
    if request.method == "POST":
        user_question = request.form.get("question", "").strip()
        
        if "힌트" in user_question:
            if hint_count < MAX_HINT:
                response = hints[hint_count]
                hint_count += 1
            else:
                response = "더 이상 힌트를 제공할 수 없습니다."
        else:
            matched = False
            for key in answers:
                if key in user_question:
                    response = random.choice(answers[key])
                    matched = True
                    break
            if not matched:
                response = "질문을 이해하지 못했습니다. 키워드를 바꿔보세요."

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
