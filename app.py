from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
import os 

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

#Database Schema Class/Model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    content = db.Column(db.String(100))
    author = db.Column(db.String(50))
    avatar = db.Column(db.String(100))

    def __init__(self, title,content, author, avatar):
        self.title = title
        self.content = content
        self.avatar = avatar
        self.author = author

#Blog Post Schema
class BlogPostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content', 'author', 'avatar')

blogpost_schema = BlogPostSchema()
blogposts_schema = BlogPostSchema(many=True)

@app.route('/post', methods=['POST'])
def add_post():
    title = request.json['title']
    content = request.json['content']
    author = request.json['author']
    avatar = request.json['avatar']

    new_post = BlogPost(title, content, author, avatar)

    db.session.add(new_post)
    db.session.commit()

    return blogpost_schema.jsonify(new_post)

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello world'})

if __name__ == "__main__":
    app.run(debug=True)

