import functools
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db

bp = Blueprint('review', __name__)

@bp.route('/')
def home():
    return render_template('review/home.html')

@bp.route('/about')
def about():
    return render_template('review/about.html')

@bp.route('/<page_name>')
def other_page(page_name):
    response = make_response(render_template('review/404.html'), 404)
    return response
