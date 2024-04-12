from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, SelectField,PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo
from models import FOOD,User

class FoodForm(FlaskForm):
    name = StringField('Name:',validators=[DataRequired('This field is required.')])
    category = SelectField('Category:',choices=[('meat','Meat'),('vegetable','Vegetable'),('fish','Fish')
                                                ,('fruit','Fruit'),('bean','Bean'),('egg_and_milk','Egg_and_Milk')
                                                ,('mushroom','Mushroom'),('processed_food','Processed_food'),('others','Others')])
    date = DateField('Expiration Date:',validators=[DataRequired('This field is required.')])
    memo = TextAreaField('Memo:')
    submit = SubmitField('Submit')
    
class FoodNeededForm(FlaskForm):
    name = StringField('Name:',validators=[DataRequired('This field is required.')])
    memo = TextAreaField('Memo:')
    submit = SubmitField('Submit')
    
class LoginForm(FlaskForm):
    username = StringField('User Name:', validators=[DataRequired('This field is required.')])
    password = PasswordField('Password:',validators=[Length(4,20,'Password must be at 4~20 characters.')])
    submit = SubmitField('Login')

class SignUpForm(FlaskForm):
    username = StringField('User Name:', validators=[DataRequired('This field is required.')])
    password = PasswordField('Password:',validators=[Length(4,20,'Password must be at 4~20 characters.'),EqualTo('confirm_password','Password does not match with confirm password.')])
    confirm_password = PasswordField('Confirm Password:')
    submit = SubmitField('Signup')
    
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username is already in use.')
        
    def validate_password(self, password):
        if not (any(c.isalpha() for c in password.data) and 
                any(c.isdigit() for c in password.data) and 
                any(c in '!@#$%*^()' for c in password.data)):
            raise ValidationError('Password must contain alphanumeric characters and symbols:! `#$%*^().')