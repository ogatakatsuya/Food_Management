from flask import Blueprint,render_template, request, redirect, url_for, flash
from models import db, FOOD, User
from forms import LoginForm, SignUpForm
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route("/",methods=["POST","GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user  = User.query.filter_by(username = username).first()
        
        if user is not None and user.check_password_hash(password):
            login_user(user)
            return redirect(url_for("food.index"))
        flash("ユーザー名かパスワードが誤っています")
    return render_template("auth/login_form.html", form=form)

@auth_bp.route("/logout",methods=["POST","GET"])
@login_required
def logout():
    logout_user()
    flash("ログアウトしました")
    return redirect(url_for("auth.login"))

@auth_bp.route("/register",methods=["POST","GET"])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash("ユーザー登録しました")
        
        return redirect(url_for("auth.login"))
    return render_template("auth/register_form.html",form=form)