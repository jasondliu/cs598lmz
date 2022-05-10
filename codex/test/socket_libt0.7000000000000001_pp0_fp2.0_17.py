import socket
import time

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.shortcuts import render
from django.conf import settings

from .models import Project, ProjectLink, ProjectImage, ProjectMedia
from .forms import ProjectForm, ProjectLinkFormSet, ProjectImageFormSet, ProjectMediaFormSet


def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects})


@user_passes_test(lambda u: u.is_staff)
def project_add(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        formset_links = ProjectLinkFormSet(request.POST)
