# config.py


import os

# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = os.urandom(24)

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)