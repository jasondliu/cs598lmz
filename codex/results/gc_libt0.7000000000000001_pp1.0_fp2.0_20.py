import gc, weakref
import logging

from django.core.exceptions import ImproperlyConfigured

from moztrap import model

from moztrap.view.lists import filters
from moztrap.view.utils.ajax import ajax

from .. import forms

from moztrap import model



logger = logging.getLogger(__name__)



@ajax()
def save_tags_to_manifests(request):
    """Save the specified tags to the specified manifests."""
    manifests = request.POST.getlist("manifests")
    tags = request.POST.getlist("tags")
    if not manifests or not tags:
        return {
            "status": "failure",
            "message": "No manifests and/or tags were specified",
            }

    # get the tag objects
    tag_objects = []
    for t in tags:
        try:
            tag_objects.append(model.Tag.objects.get(pk=t))
        except model.Tag.DoesNotExist:
            return {
                "status": "
