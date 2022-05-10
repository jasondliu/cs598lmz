import weakref

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.fields.related import RECURSIVE_RELATIONSHIP_CONSTANT
from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor
from django.db.models.fields.related_descriptors import ManyToManyDescriptor
from django.db.models.fields.related_descriptors import ReverseManyToOneDescriptor
from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager
from django.db.models.fields.related_descriptors import create_reverse_many_to_many_manager
from django.db.models.fields.related_descriptors import create_reverse_one_to_one_manager
from django.db.models.fields.related_descriptors import create_forward_many_to_one_manager
from dj
