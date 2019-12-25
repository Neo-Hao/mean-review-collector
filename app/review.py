import functools
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db
from app.auth import login_required

bp = Blueprint('review', __name__)

# home page of the web application
@bp.route('/')
def home():
    return render_template('review/home.html')

# about page
@bp.route('/about')
def about():
    return render_template('review/about.html')

# # 404 error
# @bp.route('/<page_name>')
# def other_page(page_name):
#     response = make_response(render_template('review/404.html'), 404)
#     return response

# user dashboard
# login required
@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('review/dashboard.html')
