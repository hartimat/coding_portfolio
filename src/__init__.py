###############################################################################
# FILENAME: __init__.py                                                       #
# PROJECT: portfolio_website                                                  #
# AUTHOR: Matt Hartigan                                                       #
# DATE: 11-August-2021                                                        #
# DESCRIPTION: __init__.py file for src directory in portfolio_website project#
###############################################################################

# IMPORTS
import os
from flask import Flask
from flask_bootstrap import Bootstrap
from . import db
from . import blueprints


# FUNCTIONS
def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'src.sqlite'),
    )

    if test_config==None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize bootstrap
    Bootstrap(app)

    # Initialize database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(blueprints.main)

    return app