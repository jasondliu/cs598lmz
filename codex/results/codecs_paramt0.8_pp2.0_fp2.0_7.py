import codecs
codecs.register_error('surrogate_escape', codecs.backslashreplace)

import os

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.utils.translation import ugettext as _

from PIL import Image
from PIL.ExifTags import TAGS
from PIL import ImageFile
ImageFile.MAXBLOCK = 2**20 # default is 64k


from backcap.forms import AddPhotoForm, EditPhotoForm, EditAlbumForm, AddAlbumForm, AddNoteForm, EditNoteForm
from backcap.models import Album, Photo, Note, PhotoNote
from backcap.utils import geocode_from_exif
from backcap.tasks import create_thumbs
from backcap.utils import redirect_with_query

from tagging.models import TaggedItem, Tag
from tagging.utils import get_tag
import tagging
