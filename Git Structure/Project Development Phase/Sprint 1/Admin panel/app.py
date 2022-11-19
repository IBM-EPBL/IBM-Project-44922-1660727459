from flask import Flask,request,render_template
import ibm_db
from db import *
app = Flask(__name__)
import ibm_db

conn = ibm_db.connect(dbconnect(), "", "")

@app.route('/')
def login():  # put application's code here
     return render_template("Login.html")
@app.route('/login',methods=['POST'])
def page():
     return render_template("registration.html")
@app.route('/register')
def register():
    print("checked")
    username1 = request.form['username']
    password1 = request.form['password']
    sql = "SELECT * FROM user WHERE username=?"
    statement = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(statement, 1, username1)
    ibm_db.execute(statement)
    acc = ibm_db.fetch_assoc(statement)
    if acc:
        print("username already exists")
        return render_template("registration.html")
    else:
        sql = "INSERT INTO user(username,password) values(?,?)"
        statement = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(statement, 1, username1)
        ibm_db.bind_param(statement, 2, password1)
        ibm_db.execute(statement)
        print("created")
        return render_template("Login.html")


if __name__ == '__main__':
    app.run()
