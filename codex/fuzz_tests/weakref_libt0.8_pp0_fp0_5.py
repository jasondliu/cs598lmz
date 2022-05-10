import weakref
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship, backref, object_mapper
from sqlalchemy.orm.session import object_session
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.sql import func, exists, and_, or_, not_
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import select, column
from ckan.model import *

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

# Define some commonly used helpers to generate common SQL expressions
def text_query(column, query, type='plain', op='like'):
    """
    Generate a case-insensitive sqlalchemy filter expression based on the query type.

    :param query: A string containing the user's query
    :param type: The type of query. Valid options are:

        *
