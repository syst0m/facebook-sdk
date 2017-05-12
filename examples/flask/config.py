from os import path

# App details
BASE_DIRECTORY = path.abspath(path.dirname(__file__))
DEBUG = True
SECRET_KEY = '09ace78fdc3591c2b22a8fa08a5ba618'

# Database details
SQLALCHEMY_DATABASE_URI = '{0}{1}'.format('sqlite:///',
                                          path.join(BASE_DIRECTORY, 'app.db'))
