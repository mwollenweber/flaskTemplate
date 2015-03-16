import traceback
import sys

from flask import render_template, redirect, session, url_for, request, g, Flask, make_response, jsonify
from flask.ext.login import current_user, login_required

from . import main

@main.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@main.route('/', methods=['GET', 'POST'])
def index():
    data = []
    return render_template('intro.html')

@main.route('/about', methods=['GET', 'POST'])
def about():
    data = []
    return render_template('about.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    data = []
    return render_template('contact.html')

@main.route('/profiles/', methods=['GET', 'POST'])
def profiles():
    data = []
    return render_template('profile.html')

@main.route('/services', methods=['GET', 'POST'])
def services():
    data = []
    return render_template('index.html')



