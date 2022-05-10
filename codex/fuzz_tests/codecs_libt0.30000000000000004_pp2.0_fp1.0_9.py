import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import subqueryload
from sqlalchemy.orm import contains_eager
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func
from sqlalchemy.sql import label
from sqlalchemy.sql import select
from sqlalchemy.sql import and_
from sqlalchemy.sql import or_
from sqlalchemy.sql import not_
from sqlalchemy.sql import exists
from sqlalchemy.sql import text
from sqlalchemy.sql.expression import cast
from sqlalchemy.sql.expression import case
from sqlal
