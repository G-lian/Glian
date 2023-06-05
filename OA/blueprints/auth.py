from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from exts import db, mail
from flask_mail import Message
import string
import random
from models import UserModel, EmailCaptchaModel
from .forms import RegisterForm

# /auth
bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/login')
def login():
    return render_template("login.html")

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        # 验证用户提交的邮箱和验证码是否对应且正确
        # 表单验证：flask-wtf: wtforms
        form = RegisterForm(request.form)
        if form.validate():
            return "success"
        else:
            errors = form.errors  # 获取表单错误信息
            return jsonify(errors=errors)  # 返回包含错误信息的响应
        
        
# bt.route: 如果没有指定methods参数，默认就是get请求
# @bp.route('/captcha/email', methods=['POST']),这样以后别人只能用post请求
@bp.route('/captcha/email')
def get_email_captcha():
    # 传参数
    # /captcha/email/<email>
    # /captcha/email?email=xxx@qq.com
    email = request.args.get('email')
    # 4/6随机的数字，字母，数字和字母组合
    source = string.digits*4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    # I/O: Input/Output
    message = Message(subject="学习注册验证码", recipients=[email], body=f"您的验证码是：{captcha}")
    mail.send(message)
    # 缓存：memcached/redis
    # 用数据库的方式存储（临时）
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTful API
    # {code: 200/400/500, message: "", data: {}}
    return jsonify({"code": 200, "message": "", "data": None})



@bp.route('/mail/test')
def mail_test():
    message = Message(subject="邮箱测试", recipients=["1292130291@qq.com"], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功"