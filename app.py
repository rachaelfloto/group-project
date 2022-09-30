from flask import Flask, render_template, request, redirect
from ticket import Ticket, query_tickets

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template("home.html", tickets=query_tickets())


# New section to link form
@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        ticketdata = request.form
        Ticket(ticketdata["name"], ticketdata["date"], ticketdata["problem"]).add()
        return redirect("/listtickets")
    return render_template("newticket.html")


@app.route('/newticket')
def newticket():
    return render_template("newticket.html", ticket=query_tickets())


@app.route('/listtickets')
def listtickets():
    return render_template("listtickets.html", tickets=query_tickets())


if __name__ == '__main__':
    app.run()
