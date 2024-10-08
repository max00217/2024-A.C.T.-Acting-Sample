from . import db
from datetime import datetime

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  content = db.Column(db.Text, nullable=False)
  author = db.Column(db.String(50), nullable=False)
  time_posted = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return f'<Post {self.title}>'