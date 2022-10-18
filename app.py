from multiprocessing.connection import wait
import time
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for, redirect, session
from progress.Python.option1 import *
from flask_mysqldb import MySQL

####################### Page Set Up #######################


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.secret_key = "skey"

# Connecting to the mysql database #

app.config['MYSQL_HOST'] = "zestea.cht6su9dthtx.us-east-2.rds.amazonaws.com",
app.config['MYSQL_USER'] = "admin"
app.config['MYSQL_PASSWORD'] = "Ethopia15"
app.config['MYSQL_DB'] = "Zestea"

mysql = MySQL(app)




# prep SRR15202685 #
#============ Runs the home page =============#
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == "POST":
        if request.form["input_method"] == "Accension #":
            acn = request.form["main1"]
            session["acn"] = acn
        elif request.form["input_method"] == "File":
            pass

        


        return redirect(url_for("step1"))


    else:
        if "sin" not in session:
            return render_template('index.html', logsin = '<li><a href="login">Log In</a></li>' )
        # elif "sin" in session:
        #     return render_template('index.html', logsin = '<li><a href="account">Account</a></li>' )
    
    return render_template('index.html', logsin = '<li><a href="login">Log In</a></li>' )


@app.route('/loading', methods=['GET','POST'])
def step1():
    task_id = "GA1001"
    if request.method == "GET":
        if "acn" in session:
            acn = session["acn"]
            script = prefetch(acn)
            script

    return render_template("loading1.html" , GA = task_id)


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        pswrd = request.form["password"]
        usrn = request.form["username"]

        if pswrd == "123" and usrn == "taerko":
            session["sin"] = "Pass"
            return render_template("index.html")
        else:
            if "sin" not in session:
                return render_template('login.html', logsin = '<li><a href="login">Log In</a></li>' )
            elif "sin" in session:
                return render_template('login.html', logsin = '<li><a href="account">Account</a></li>' )




    if "sin" not in session:
        return render_template('login.html', logsin = '<li><a href="login">Log In</a></li>' )
    elif "sin" in session:
        return render_template('login.html', logsin = '<li><a href="account">Account</a></li>' )


@app.route('/crac', methods=['GET','POST'])
def crac():
    if request.method == "POST":
        email = request.form["email"]
        pswrd = request.form["password"]
        repswrd = request.form["repassword"]
        usrn = request.form["username"]

        if pswrd == repswrd:

            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO Users(Username, Passw, Email) VALUES (%s, %s, %s)", (usrn, pswrd,email))
            mysql.connection.commit()
            cursor.close()



        



    if "sin" not in session:
        return render_template('create_ac.html', logsin = '<li><a href="login">Log In</a></li>' )
    elif "sin" in session:
        return render_template('create_ac.html', logsin = '<li><a href="account">Account</a></li>' )



@app.route('/account', methods=['GET','POST'])
def account():
    
    if "sin" not in session:
        return render_template('account.html', logsin = '<li><a href="login">Log In</a></li>' )
    elif "sin" in session:
        return render_template('account.html', logsin = '<li><a href="account">Account</a></li>' )



if __name__ == '__main__':
    app.run(debug=True)