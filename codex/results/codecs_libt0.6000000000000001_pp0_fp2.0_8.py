import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from user.models import Profile
from .models import Post, Comment, Category, Feed, Tag, FeedPost, FeedComment
from .forms import PostForm, CommentForm, SearchForm
from .tasks import send_new_post_notification
from .utils
