from bz2 import BZ2Decompressor
BZ2Decompressor.decompress(x)

# In[ ]:


# %load app/__init__.py

import os
import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_compress import Compress

# instantiate the db
db = SQLAlchemy()

# instantiate flask-compress
compress=Compress()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config and logger
    configure_app(app)
    configure_logger(app)

    # set up extensions
    configure_extensions(app)
    configure_blueprints(app)

    # register shell context
    register_shellcontext(app)

    # register logs and url slugs to remove
    register_commands(app)
    from app.utils import DeleteDocs
    DeleteDocs().run()

    # shell context for flask cli
    return app


def configure_app(app):
    """Load configuration settings."""
    # set app settings
