from flask import Blueprint
from flask import request
from flask import jsonify
from .models import db, Post

bp = Blueprint('main', __name__)

@bp.route('/')
def hello():
  return "Hello, Flask!"

@bp.route('/posts', methods=['POST'])
def create_post():
  data = request.get_json()
  new_post = Post(title=data['title'], content=data['content'], author=data['author'])
  db.session.add(new_post)
  db.session.commit()
  return jsonify({"message": "게시물 생성됨."}), 201 ,{'Content-Type': 'application/json; charset=utf-8'}

@bp.route('/posts', methods=['GET'])
def get_posts():
  posts = Post.query.all()
  return jsonify([{"id": post.id, "title": post.title, "content": post.content, "author": post.author, "time_posted": post.time_posted} for post in posts])

@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
  post = Post.query.get_or_404(id)
  return jsonify({"id": post.id, "title": post.title, "content": post.content, "author": post.author, "time_posted": post.time_posted})

@bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
  post = Post.query.get_or_404(id)
  data = request.get_json()
  post.title = data['title']
  post.content = data['content']
  post.author = data['author']
  db.session.commit()
  return jsonify({"message": "게시물 업데이트됨."})

@bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
  post = Post.query.get_or_404(id)
  db.session.delete(post)
  db.session.commit()
  return jsonify({"message": "게시물 삭제됨."})
