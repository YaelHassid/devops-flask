import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import boto3
from io import BytesIO
import base64


db_username = os.environ['DB_USERNAME']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
db_uri = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
print(f"Connecting db @{db_uri}")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy()
db.init_app(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(250), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
obj = s3.get_object(Bucket="best-practice-bucket-of-yaya", Key="hello.gif")
gifi = obj['Body'].read()
gifi_base64 = base64.b64encode(gifi).decode('utf-8')

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        u_name = request.form['name']
        u_email = request.form['email']
        new_user = User(name=u_name, email=u_email)
        db.session.add(new_user)
        db.session.commit()
        return render_template('say_hello.html', name=u_name, pic=gifi_base64)
    else :
        return render_template('home.html')


@app.route('/say_hello')
def say_hello(name, pic):
    return render_template('say_hello.html', name=name, pic=gifi_base64)

@app.route('/users')
def show_users():
    users = User.query.all()
    user_list = {}
    for user in users:
        user_list[user.id] = [user.name, user.email]
    return user_list

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)