"""Blogly application."""

from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'imsocool'

app.debug = True
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def redirect_to_users():
    """ Redirects to the list of users. """

    return redirect('/users')


@app.route('/users')
def show_index():
    """ Show all users list and link to add-user """
    
    users = User.query.all()
    
    return render_template('users_list.html', users=users)


@app.route('/users/new')
def show_create_page():
    """ Show the new user creation form """

    return render_template('user_form.html')


@app.route('/users/new', methods=["POST"])
def handle_new_user():
    """ Obtain Form info and place into database """

    return redirect('/users')


@app.route('/users/<int:id>')
def show_user_profile(id):
    """ Return the user's profile page """

    return render_template('user_profile.html')


@app.route('/users/<int:id>/edit')
def show_edit_page(id):
    """ Display the edit page for selected user """

    return render_template('edit_page.html', id=id)

@app.route('/users/<int:id>/edit', methods=["POST"])
def handle_edit(id):
    """ Obtain Form info and update the database """

    return redirect('/users')


@app.route('/users/<int:id>/delete', methods=["POST"])
def delete_user(id):
    """ Delete the user by id from the database and redirect
        to the users list """

    return redirect('/users')





