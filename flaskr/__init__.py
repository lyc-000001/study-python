import os

from flask import Flask, request, jsonify
from . import auth
from . import blog
from flask_jwt_extended import JWTManager, jwt_required, verify_jwt_in_request

app = Flask(__name__, instance_relative_config=True)


def create_app(test_config=None):
    # create and configure the app

    app.config["JWT_SECRET_KEY"] = "super-secret"
    jwt = JWTManager(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp1)

    return app


# 添加全局校验token
@app.before_request
def check_token():
    # 登录路由或者其他不需要 token 的路由不做检查
    if request.path in ['/auth/login']:
        return

    # 其余路由强制验证 token
    try:
        verify_jwt_in_request()
    except Exception as e:
        return jsonify({"msg": str(e)}), 401
