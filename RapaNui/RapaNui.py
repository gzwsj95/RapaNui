from flask import Flask, render_template, request, redirect, url_for, session,abort
import config
import pymysql
pymysql.install_as_MySQLdb()
from models import User
from exts import db

app = Flask(__name__)
#加载config.py配置文件
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = User.query.filter(User.username == username, User.password == password).first()
        if confirm:
            session['user_id'] = confirm.id  #记录登录用户名-储存到session
            return redirect(url_for("index")) #登录成功-跳转到index视图函数-返回index.html首页
        else:
            return u'登录失败'
    else:
        return render_template('login.html')

@app.route('/logout/')
def logout():
    login_confirm = session.get('user_id')
    if login_confirm:
        session.clear()
    else:
        abort(404)
    return redirect(url_for('login'))

@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        username = request.form.get('username')
        telephone = request.form.get('telephone')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #手机号和密码验证
        confirm = User.query.filter(User.telephone == telephone).first()
        if confirm:
            return u"手机号重复!"
        else:
            if password1 != password2:
                return u"密码不等"
            else:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("login"))

#上下文管理器
@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        return {'user':user}

    return {}  #必须返回一个空字典



if __name__ == '__main__':
    app.run()
