from flask import Flask,render_template


app = Flask(__name__)

@app.route("/hi/<name1>")
def hi_template_render(name1):
    return render_template('hi.html',name=name1)
#name1-> 내가 보내는 변수명, name-> 받는 인자명

@app.route("/")#메인페이지 들어옴
def home():
    return "<h1>메인 페이지</h1>"
@app.route("/about")
def about():
    return "<h1>소개 페이지</h1>"
@app.route("/test/<text>")
def route_sample(text):
    return f"<h1>{text}</h1>"

@app.route("/age/<num>") # 타입 없음->text로 받기때문에 타입이 str이 됨
def age_any(num):
    return f"<h1>{num} 살 — 타입은 {type(num).__name__}</h1>"
@app.route("/age2/<int:num>") # 정수만-> 정수로 받기때문에 타입이 int로 나옴
def age_int(num):
    return f"<h1>{num} 살 — 타입은 {type(num).__name__}</h1>"




#이게 중간에 들어가면 이 이후는 실행이 안됨
if __name__=="__main__":
    app.run(debug=True)