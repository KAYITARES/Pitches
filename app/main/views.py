from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm,UpdateProfile,PitchForm,CommentForm
from ..models import User,Pitche,Comment
from flask_login import login_required,current_user
from .. import db

@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    all_pitches =Pitche.query.all()
  
    title = 'Home'
    return render_template('index.html', title = title,all_pitches=all_pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/pitch/new', methods=['GET','POST'])
@login_required
def create_pitches():
    form = PitchForm()
    if form.validate_on_submit():
        category=form.category.data
        content=form.content.data
        new_pitch = Pitche(content=content,category=category, user=current_user)
        new_pitch.save_pitch()

        return redirect(url_for('main.index'))

    return render_template('pitch.html',form = form)   

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def add_comments(id):
    form = CommentForm()
    if form.validate_on_submit():
        comment=form.comment.data
        new_comment = Comment(comment=comment,pitches_id=id, user=current_user)
        
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('main.index'))
    comment=Comment.query.filter_by(pitches_id=id).all()


    return render_template('comment.html',comment=comment,form =form)   
@main.route('/category/<cat>')
def category(cat):
    my_category = Pitch.get_category(cat)

    title = f'{cat} category | One Minute Pitch'

    return render_template('category.html', title=title, category=my_category)