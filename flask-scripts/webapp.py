import time
from flask import *
import sys
import psycopg2


app = Flask(__name__)
app.secret_key = 'long life to the queen'


def  new_user(pseudo,mdp):
    try:
        conn = psycopg2.connect("host=dbserver dbname=jpourtier user=jpourtier")
        print('Connected to the database')
        cur = conn.cursor()
        command_insert = 'insert into mini_chat.Username values (\'' + pseudo + '\',\'' + mdp + '\');'
        try:
            cur.execute(command_insert)
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('hello'))
        except Exception as e :
            return "le pseudo est déjà utilisé" + render_template("Accueil.html")

    except Exception as e :
        return "impossible de se connecter à la base de donnée :" + str(e)


def login(pseudo,mdp):
    try:
        conn = psycopg2.connect("host=dbserver dbname=jpourtier user=jpourtier")
        print('Connected to the database')
        cur = conn.cursor()
        command = 'select * from mini_chat.Username where pseudo = \'' + pseudo + '\';'
        try:
            cur.execute(command)
            saucisse = cur.fetchall()
            nickname = saucisse[0]
            if nickname[1] == mdp:
                cur.close()
                conn.close()
                session['username'] = pseudo
                return display_chat()
            else :
                cur.close()
                conn.close()
                return "Mot de passe invalide" + render_template("Accueil.html")
            cur.close()
            conn.close()
            return display_chat()
        except Exception as e :
            return "Le pseudo n'existe pas" + render_template("Accueil.html")
    except Exception as e :
        return "impossible de se connecter à la base de donnée :" + str(e)

@app.route("/display_chat", methods=['POST','GET'])
def display_chat():
    try:
        conn = psycopg2.connect("host=dbserver dbname=jpourtier user=jpourtier")
        print('Connected to the database')
        cur = conn.cursor()
        command = 'select * from mini_chat.chat order by id DESC LIMIT 10;'
        try:
            cur.execute(command)
            merguez = cur.fetchall()
            merguez = reversed(merguez)
            cur.close()
            conn.close()
            return render_template("chat.html",merguez = merguez)
        except Exception as e :
            return "ERROR 404: " + command_insert + " : " + str(e)
    except Exception as e :
        return "impossible de se connecter à la base de donnée :" + str(e)


def insert_display_chat(pseudo,message):
    try:
        conn = psycopg2.connect("host=dbserver dbname=jpourtier user=jpourtier")
        print('Connected to the database')
        cur = conn.cursor()
        command_insert = 'insert into mini_chat.chat values (%s,%s);'
        try:
            cur.execute(command_insert,(pseudo,message))
            conn.commit()
            cur.close()
            conn.close()
            return display_chat()
        except Exception as e :
            return "ERROR 404" + command_insert + " : " + str(e)
    except Exception as e :
        return "impossible de se connecter à la base de donnée :" + str(e)









@app.route("/")
def hello():
    session.pop('username', None)
    return  render_template("Accueil.html")


@app.route("/after_form", methods=['POST'])
def after_form():
    print("I got it!")
    pseudo = session['username']
    return insert_display_chat(pseudo ,request.form['message'])

@app.route("/log", methods=['POST'])
def log():
    print("I got it!")
    return login(request.form['pseudo'],request.form['mdp'])

@app.route("/new_user", methods=['POST'])
def create():
    return render_template("new_user.html")

@app.route("/confirm",methods=['POST'])
def confirm():
    return new_user(request.form['pseudo'],request.form['mdp'])

@app.route("/end",methods=['POST'])
def end():
    session.pop('username', None)
    return "Vous êtes déconnecté" + render_template("Accueil.html")











if __name__ == "__main__":
   app.run(debug=True)
