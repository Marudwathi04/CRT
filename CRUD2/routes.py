from flask import render_template, url_for, flash, redirect, request, Blueprint
from app import db
from models import User
from templates import register, login, EditUserForm

main = Blueprint('main', __name__)

def init_routes(app):
    app.register_blueprint(main)

@main.route("/")
@main.route("/home")
def home():
    return render_template('base.html')

@main.route("/register", methods=['GET', 'POST'])
def register():
    form = register()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    form = login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            flash('You have been logged in!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route("/users")
def users():
    users = User.query.all()
    return render_template('user_list.html', title='Users', users=users)

@main.route("/user/<int:user_id>/edit", methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = EditUserForm()
    if form.validate_on_submit():
        user.username = form.username.data
        user.password = form.password.data
        db.session.commit()
        flash('User has been updated!', 'success')
        return redirect(url_for('main.users'))
    elif request.method == 'GET':
        form.username.data = user.username
        form.password.data = user.password
    return render_template('user_edit.html', title='Edit User', form=form, user=user)

@main.route("/user/<int:user_id>/delete", methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User has been deleted!', 'success')
    return redirect(url_for('main.users'))
