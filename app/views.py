# app/views.py

from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Post
from app import db

bp = Blueprint('views', __name__)

@bp.route('/')
@bp.route('/posts')
def index():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)

@bp.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@bp.route('/create-post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('views.post', post_id=post.id))
    return render_template('create_post.html')
