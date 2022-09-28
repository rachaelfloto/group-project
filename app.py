from flask import Flask, render_template
from data import Articles

# from ticket import Ticket

app = Flask(__name__)
app.debug = True

Articles = Articles()


@app.route('/')
def index():
    return render_template('home.html')


# New section to link form
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form["name"])
        print(request.form["date"])
        print(request.form["problem"])
        return
    return render_template("newticket.html")


@app.route('/newticket')
def newticket():
    return render_template('newticket.html')


@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)


@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)


if __name__ == '__main__':
    app.run()
