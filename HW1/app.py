from flask import Flask,render_template


app = Flask(__name__)


@app.route("/")#메인페이지 들어옴
def home():
    return render_template('home.html')
#"<h1>22011645_김준혁</h1>"


@app.route("/profile")#취미
def hobbies_template_render():
    hobbies1 = ["게임", "영화 감상", "웹툰"]
    return render_template('profile.html',hobbies=hobbies1)



@app.route("/greet/<name>")#인사
def hi_template_render(name):
    return render_template('hi.html',name=name)





#이게 중간에 들어가면 이 이후는 실행이 안됨
if __name__=="__main__":
    app.run(debug=True)