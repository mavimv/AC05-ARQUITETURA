import os
from flask import render_template, request
from __init__ import app, db
from models import Post

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        post = Post(
            text=request.form['text']
        )
        db.session.add(post)
        db.session.commit()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)


if __name__ == "__main__":
    db.create_all()
    port = 8080
    app.run(host='0.0.0.0', port=port, debug=True)
