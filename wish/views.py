from flask import Blueprint,render_template, request, redirect, url_for, flash
from models import db, FOOD, User, FOOD_NEEDED
from forms import FoodForm,FoodNeededForm
from flask_login import login_required, current_user

wish_bp = Blueprint('wish', __name__, url_prefix='/wish')

@wish_bp.route("/index")
@login_required
def index_wish():
    foods = FOOD_NEEDED.query.filter_by(user_id = current_user.id).all()
    return render_template("wish/needs.html", foods_needed=foods)

@wish_bp.route("/create", methods=["POST","GET"])
@login_required
def create_wish():
    form = FoodNeededForm()
    if form.validate_on_submit():
        name = form.name.data
        memo = form.memo.data
        food = FOOD_NEEDED(name=name, memo=memo, user_id = current_user.id)
        db.session.add(food)
        db.session.commit()
        
        flash("Registration Succeeded!")
        
        return redirect(url_for("wish.index_wish"))
    return render_template("wish/create_wish.html", form=form)

@wish_bp.route("/update/<int:food_id>", methods=["POST","GET"])
@login_required
def update_wish(food_id):
    target_data = FOOD_NEEDED.query.filter_by(id=food_id, user_id=current_user.id).first_or_404()
    form = FoodNeededForm(obj=target_data)
    
    if request.method == "POST" and form.validate():
        target_data.name = form.name.data
        target_data.memo = form.memo.data
        db.session.commit()
        
        flash("Edit Succeeded!")
        
        return redirect(url_for("wish.index_wish"))
    return render_template("wish/update_wish.html",form=form, edit_id=target_data.id)

@wish_bp.route("/delete/<int:food_id>")
@login_required
def delete_wish(food_id):
    food = FOOD_NEEDED.query.filter_by(id=food_id, user_id=current_user.id).first_or_404()
    db.session.delete(food)
    db.session.commit()
    
    flash("Delete Succeeded!")
    
    return redirect(url_for("wish.index_wish"))