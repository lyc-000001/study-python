from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp1 = Blueprint('blog', __name__, url_prefix='/blog')


@bp1.route('/index')
def index1():
    return 'test'


@bp1.route('/test')
def test():
    return 'hello'


@bp1.route('/about')
def about():
    # 使用 endpoint 'home' 动态生成 URL
    return 'Go to homepage'
