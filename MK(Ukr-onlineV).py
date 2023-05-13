import flask
import sqlite3
from werkzeug.exceptions import abort
import random
import config

def return_connect ():
    connect = sqlite3.connect ("answers.db")
    connect.row_factory = sqlite3.Row
    return connect

def close (connect, kursor):
    connect.close ()
    kursor.close ()

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = config.password

def main ():
    app = flask.Flask (__name__)

if __name__ == "__main__":
    main ()

connect = sqlite3.connect ("answers.db")
kursor = connect.cursor ()

kursor.execute ("""SELECT
id FROM qui ORDER BY id
""")
qui_ids = kursor.fetchall ()
qui_ids = [len(qui_ids)][0]

que_dict = {}

for qui_id in range(1, qui_ids+1):
    select = """SELECT
    que.que,
    que.id,
    que.right_answer,
    que.wrong_answer1,
    que.wrong_answer2,
    que.wrong_answer3
    FROM zwjazok, que
    WHERE zwjazok.qui == (?)
    AND que.id == zwjazok.id"""
    kursor.execute (select, [qui_id])
    que = kursor.fetchall ()
    que_dict[str(qui_id)] = que

kursor.execute ("""SELECT
    que.que,
    que.id,
    que.right_answer,
    que.wrong_answer1,
    que.wrong_answer2,
    que.wrong_answer3
    FROM que""")
dcaq = kursor.fetchall ()
que_dict["all"] = dcaq

@app.route("/")
@app.route("/main/")
def index ():
    connect = return_connect ()
    kursor = connect.cursor ()
    kursor.execute ("""SELECT * FROM qui""")
    quis = kursor.fetchall ()
    flask.session["qui"] = que_dict
    flask.session["counter"] = 0
    return flask.render_template ("index.html", quis = quis)


def questions_router ():
    qui = flask.request.args.get ("id")
    if str(type(flask.session.get ("qui"))) == "<class 'dict'>":
        quess = flask.session.get ("qui")[str(qui)]
        flask.session["qui"] = quess
        random.shuffle (quess)
        all = len(flask.session ["qui"])
        flask.session ["result"] = [0, all]
    else:
        quess = flask.session.get ("qui")
    if len(flask.session.get ("qui")) > 0:
        ques = quess[0]
        answers = list(ques[2:6])
        que = ques[0]
        random.shuffle (answers)
        return flask.render_template ("qui_window.html", id = ques[1],
        que=que,
        answer1=answers[0],
        answer2=answers[1],
        answer3=answers[2],
        answer4=answers[3],
        qui_id = qui)
    else:
        return flask.redirect (flask.url_for ("total"))
app.add_url_rule ("/questions/", "questions", questions_router, methods = ["GET", "POST"]) #Можливо це зміниться 

@app.route("/")
@app.route("/total/")
def total ():
    right = flask.session.get ("result")[0]
    all = flask.session.get ("result")[1]
    widsotok = right/all * 100
    widsotok = int(round(widsotok, 0))
    flask.flash ("Відсоток правильних відповідей:" + str(widsotok) + "%.")
    return flask.redirect (flask.url_for ("index"))

def result ():
    id_ = flask.request.args.get ("id")
    qui_id = flask.request.args.get ("qui_id")
    if flask.request.method == "POST":
        here = flask.request.form.get (str(id_))
        connect = sqlite3.connect ("answers.db")
        kursor = connect.cursor ()
        kursor.execute ("""SELECT right_answer FROM que
        WHERE id == (?)""", [id_])
        data = kursor.fetchone ()[0]
        flask.session["qui"] = flask.session["qui"][1:]
        if data == here:
            flask.session ["result"][0] += 1
            result_ = "Правильно!"
        else:
            result_ = "Неправильно!"
        return flask.render_template ("result_window.html", result_ = result_, qui_id = qui_id)
    else:
        abort (404)
app.add_url_rule ("/result/", "result", result, methods = ["GET", "POST"]) #Можливо це зміниться



app.run (debug = True)

#close (connect, kursor)