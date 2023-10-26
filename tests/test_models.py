import pytest
from app.models import User, Post, Comment

def test_user_model():
    user = User(username='testuser', email='test@example.com', password='password')
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'

def test_post_model():
    post = Post(title='Test Post', content='Test Content', user_id=1)
    assert post.title == 'Test Post'
    assert post.content == 'Test Content'
    assert post.user_id == 1

def test_comment_model():
    comment = Comment(content='Test Comment', user_id=1, post_id=1)
    assert comment.content == 'Test Comment'
    assert comment.user_id == 1
    assert comment.post_id == 1
