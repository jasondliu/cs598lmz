import socket
import threading

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson

from django_socketio import events, broadcast, broadcast_channel, NoSocket
from django_socketio.exceptions import SocketIOError

from .models import ChatRoom, ChatUser, ChatMessage


@login_required
def index(request):
    """
    Index page. Shows a list of rooms to join.
    """
    context = {
        'rooms': ChatRoom.objects.all(),
    }
    return render_to_response('chat/index.html', context, context_instance=RequestContext(request))


@login_required
