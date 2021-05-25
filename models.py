from __init__ import db
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    text = db.Column(db.String(150), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)

    def __init__(self, text):
        self.text = text
        self.date_posted = datetime.now()
