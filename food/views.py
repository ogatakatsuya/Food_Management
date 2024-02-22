from flask import Blueprint,render_template, request, redirect, url_for, flash
from models import db, FOOD, User
from forms import FoodForm
from flask_login import login_required, current_user

food_bp = Blueprint('food', __name__, url_prefix='/food')

@food_bp.route("/food/")
@login_required
def index():
    foods = FOOD.query.filter_by(user_id = current_user.id).all()
    return render_template("food/index.html", foods=foods)

@food_bp.route("/food/create", methods=["POST","GET"])
@login_required
def create():
    form = FoodForm()
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        date = form.date.data
        memo = form.memo.data
        food = FOOD(name=name, category=category, date=date, memo=memo, user_id = current_user.id)
        db.session.add(food)
        db.session.commit()
        
        flash("Registration Succeeded!")
        
        return redirect(url_for("food.index"))
    return render_template("food/create_form.html", form=form)

@food_bp.route("/food/update/<int:food_id>", methods=["POST","GET"])
@login_required
def update(food_id):
    target_data = FOOD.query.filter_by(id=food_id, user_id=current_user.id).first_or_404()
    form = FoodForm(obj=target_data)
    
    if request.method == "POST" and form.validate():
        target_data.name = form.name.data
        target_data.category = form.category.data
        target_data.date = form.date.data
        target_data.memo = form.memo.data
        db.session.commit()
        
        flash("Change Succeeded!")
        
        return redirect(url_for("food.index"))
    return render_template("food/update_form.html",form=form, edit_id=target_data.id)

@food_bp.route("/food/delete/<int:food_id>")
@login_required
def delete(food_id):
    food = FOOD.query.filter_by(id=food_id, user_id=current_user.id).first_or_404()
    db.session.delete(food)
    db.session.commit()
    
    flash("Delete Succeeded!")
    
    return redirect(url_for("food.index"))