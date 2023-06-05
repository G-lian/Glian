from flask import Flask
from exts import db, mail
import config
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate
# from flask import render_template


app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)


db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


# blueprint:用来做模块化的
# 电影，读书，音乐，xxx


# flask db init: 只需要执行一次
# flask db migrate: 将orm模型生成迁移脚本
# flask db upgrade: 将迁移脚本映射到数据库中


# @app.route('/')
# def index():
#     return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)