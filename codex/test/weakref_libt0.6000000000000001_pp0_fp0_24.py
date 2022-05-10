import weakref
import logging
from datetime import datetime
from operator import itemgetter

from sqlalchemy import Column, Integer, String, DateTime, Unicode, Boolean, ForeignKey, Text, UniqueConstraint, Index
from sqlalchemy.orm import relation, backref, synonym, class_mapper
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import object_session
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.sql.expression import desc
from sqlalchemy.ext.associationproxy import association_proxy

from zope.interface import implements
from zope.component import adapts

from repoze.who.interfaces import IAuthenticator
from repoze.who.interfaces import IChallenger
from repoze.who.interfaces import IMetadataProvider
