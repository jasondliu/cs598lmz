import weakref
from datetime import datetime
from typing import List, Optional
from uuid import uuid4

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import backref, relationship
from sqlalchemy.orm.collections import attribute_mapped_collection

from . import Base, UUIDMixin
from .attachment import Attachment
from .audit import AuditMixin
from .base import BaseMixin
from .db import db
from .project import Project
from .user import User
from .validation import ValidationMixin

__all__ = [
    "Comment",
    "CommentAttachment",
    "CommentAttachmentCollection",
    "CommentCollection",
    "CommentNotification",
    "CommentNotificationCollection",
    "CommentNotificationState",
    "CommentNotificationStateCollection",
    "CommentState",
    "CommentStateCollection",
    "CommentType",
    "CommentTypeCollection",
    "CommentUser",
    "CommentUserCollection",
    "CommentUserNotification",
    "CommentUserNotificationCollection",
    "
