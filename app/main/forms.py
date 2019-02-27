from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
# class LoginForm(FlaskForm):
#     email = StringField('Your Email Address',validators=[Required(),Email()])
#     password = PasswordField('Password',validators =[Required()])
#     remember = BooleanField('Remember me')
#     submit = SubmitField('Sign In')
class PitchForm(FlaskForm):
    
    # my_category = StringField('Category', validators=[Required()])
    my_category = SelectField('Category', choices=[('Business','Business'),('Academic','Academic'),('Political','Political'),('Technology','Technology'),('Health','Health')],validators=[Required()])
    pitch = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Submit!')

# class CommentForm(FlaskForm):
#     comment = TextAreaField('Comment', validators=[Required()])
#     submit = SubmitField('Post Comment')