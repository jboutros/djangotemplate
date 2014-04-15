from django.shortcuts import render_to_response
from django.template import RequestContext


def app_home(request, template = "home.html"):
    c = {}
    return render_to_response(template, c, context_instance=RequestContext(request))
