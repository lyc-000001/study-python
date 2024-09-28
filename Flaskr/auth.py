import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

from flask import jsonify

from flask_jwt_extended import (create_access_token, verify_jwt_in_request, jwt_required, JWTManager,
                                set_access_cookies, unset_jwt_cookies)
from Flaskr import db

bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@bp.route('/register')
def register():
    return 'register page'


@bp.route("/login", methods=["POST"])
def login():
    username = request.form.get('username')
    pwd = request.form.get('password')
    db.test1()
    access_token = create_access_token(identity=request.form.get('username'))
    response = jsonify({"msg": "login successful", 'access_token': access_token, 'code': '200'})
    return response


@bp.route("/protected", methods=["GET", "POST"])
def protected():
    msg = request.form.get('username')
    return jsonify(foo=msg)
