from flask import Blueprint,render_template, request, redirect, url_for, flash
from models import db, FOOD, User, FOOD_NEEDED
from forms import FoodForm,FoodNeededForm
from flask_login import login_required, current_user

recipe_bp = Blueprint('recipe', __name__, url_prefix='/recipe')

@recipe_bp.route("/search")
@login_required
def search():
    
    return render_template("recipe/search.html")