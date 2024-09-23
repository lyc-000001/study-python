from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('blog', __name__)


@bp.route('/index')
def index1():
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    # return render_template('blog/index.html', posts=posts)

    return 'test'


@bp.route('/test')
def test():

    return f'hello {url_for("home")}'


@bp.route('/about')
def about():
    # 使用 endpoint 'home' 动态生成 URL
    return f'Go to homepage: {url_for("home")}'
