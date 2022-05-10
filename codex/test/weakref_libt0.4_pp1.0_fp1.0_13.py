import weakref

from django.db.models.query import QuerySet
from django.db.models.signals import post_save
from django.db.models.fields import FieldDoesNotExist
from django.db.models.fields.related import (RelatedField,
                                             ReverseSingleRelatedObjectDescriptor,
                                             ReverseManyRelatedObjectsDescriptor)
from django.db.utils import DatabaseError
from django.utils.functional import curry
from django.utils.translation import ugettext as _

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.generic import GenericRelation

from django.contrib.auth.models import User

from django.contrib.comments.models import Comment
from django.contrib.comments.signals import comment_was_posted

from threadedcomments.forms import ThreadedCommentForm
from threadedcomments.util import annotate_tree_properties
from threadedcomments.util import get_tree_queryset_descriptor
