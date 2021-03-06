from flask import Blueprint, render_template, request, redirect, flash, abort, url_for
from flask_login import login_required, current_user, login_user
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
import peewee as pw
from config import Config


users_blueprint = Blueprint('users',                        
                            __name__,
                            template_folder='templates')

@users_blueprint.route("/show/<username>")
@login_required
def show(username):
    return render_template('users/show.html')

@users_blueprint.route('/new', methods = ["GET"])
def new():
    return render_template('users/new.html')

@users_blueprint.route('/create', methods = ["POST"])
def create():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    password = generate_password_hash(password)

    #create new db row
    u = User(username=username, email=email, hash=password)
    u.save()
    login_user(u)

    return redirect( url_for('users.show', username=username))




# @users_blueprint.route("/")