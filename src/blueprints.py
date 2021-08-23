###############################################################################
# FILENAME: blueprints.py                                                     #
# PROJECT: portfolio_website                                                  #
# AUTHOR: Matt Hartigan                                                       #
# DATE: 11-August-2021                                                        #
# DESCRIPTION: File that defines all blueprints for the project.              #
###############################################################################

# IMPORTS
import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from src.db import get_db


# BLUEPRINTS
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/demo/<project>', methods=['GET'])
def demo(project):
    return render_template('demo.html', project=project)

@main.route('/description/<project>', methods=['GET'])
def description(project):
    url = 'description' + str(project) + '.html'
    return render_template(url, project=project)
