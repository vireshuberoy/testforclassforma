from flask import Flask
from flask import request, render_template, redirect, url_for, session, flash
from flaskext.mysql import MySQL
from dotenv import load_dotenv
import os
import traceback
import json
import struct
import hashlib

load_dotenv()

class Server:
    def __init__(self, mysql):
        # self.mydb = mysql.connector.connect(
        #     host='localhost',
        #     user=os.getenv("MYSQL_USERNAME"),
        #     password=os.getenv("MYSQL_PASSWORD"),
        #     port=os.getenv("MYSQL_PORT"),
        #     database=os.getenv("MYSQL_DATABASE")
        # )
        # config = {
        #     host: 'db',
        #     user: "root",
        #     password: "root",
        #     port: '3306',
        #     database: 'classforma'
        # }
        # self.mydb = mysql.connector.connect(
        #     **config
        # )
        # self.mydb = mysql.connector.connect(
        #     host='db',
        #     user='root',
        #     password='root',
        #     port='3306',
        #     database='classforma'
        # )
        self.conn = mysql.connect()
        self.cursor = self.conn.cursor()

    def create_a_user(self, username, password):
        try:
            salt = os.getenv("SALT")
            random_pos = struct.unpack('i', os.urandom(4))[0] % len(password)
            part1, part2 = password[:random_pos], password[random_pos:]
            new_password = part1 + salt + part2
            final_password = hashlib.md5(bytes(new_password, 'utf-8')).hexdigest()

            sql = "INSERT INTO user_accounts (username, password, position) values (%s, %s, %s)"
            val = (username, final_password, random_pos)

            self.cursor.execute(sql, val)
            self.conn.commit()
        except:
            raise Exception("User exists") # hacky fix
        # except mysql.connector.errors.IntegrityError: # error would occur when using mysql connector, this was the way to check if a user existed or not
        #     print("oops")
        #     raise Exception("User exists")


    def does_user_exist(self, username, password):
        sql = "SELECT * FROM user_accounts WHERE username=%s"
        val = (username, )
        self.cursor.execute(sql, val)
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            return False
        rows = rows[0]

        hashed_password = rows[1]
        pos = rows[2]
        part1, part2 = password[:pos], password[pos:]
        salt = os.getenv("SALT")
        new_password = part1 + salt + part2
        final_password = hashlib.md5(bytes(new_password, 'utf-8')).hexdigest()
        if final_password == hashed_password:
            return True
        else:
            return False

    def list_all_users(self):
        sql = "SELECT * FROM user_accounts"
        self.cursor.execute(sql)

        rows = self.cursor.fetchall()

        return str(rows)

app = Flask(__name__)
app.secret_key = os.getenv("APPSECRETKEY")

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'classforma'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)
instance = Server(mysql)

@app.route('/')
def home_page():
    return render_template("home_page.html")

@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if instance.does_user_exist(username, password):
            session['logged_in'] = True
            return render_template("logged_in.html", username=request.form['username'])
        else:
            return render_template("home_page.html", error="Invalid Credentials, please try again")

@app.route('/create', methods=['POST'])
def create_user():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        try:
            instance.create_a_user(username, password)
            flash('user created')
        except Exception as e:
            if e.args[0] == "User exists": # this was for mysql connector not included with flask
                return render_template("home_page.html", error="User already exists!")
            else:
                traceback.print_exc()
                return render_template("home_page.html", error="Some error occurred. Please try again with valid data")

        return redirect(url_for("home_page"))

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("home_page"))

@app.route('/list', methods=['GET'])
def list_users():
    return instance.list_all_users()

# @app.route('/update', methods=['POST'])
# def update_user():
#     return instance.update_a_user()

# @app.route('/delete', methods=['POST'])
# def delete_user():
#     return instance.delete_a_user()

app.run(host='0.0.0.0', debug=True, port=8000)
