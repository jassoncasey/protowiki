from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context

from core.models import Protocol, Relation, json_protocols, json_relations
import json

# Create your views here.
def index(request):
  menu = loader.get_template('menu.html')
  graph = loader.get_template('graph.js')

  mc = {
    "menu_items" : [
      { "link" : "#",
        "name" : "Protocol"},
      { "link" : "#",
        "name" : "About"},
    ]
  }

  context = {
    'header' : menu.render(Context(mc)),
    'content' : graph.render(Context()),
    'footer' : "fuck you ...",
  }
  return render(request, 'base.html', context)

def flare(request):

  result = { "nodes" : [
        { "name" : "Ethernet" },
        { "name" : "IPv4" },
        { "name" : "ARP" },
        { "name" : "ICMPv4" },
      ],
      "edges" : [
        { "source" : 0, "target" : 1 },
        { "source" : 0, "target" : 2 },
        { "source" : 1, "target" : 3 },
        { "source" : 2, "target" : 3 },
        { "source" : 3, "target" : 0 },
      ],
  }

  return HttpResponse(json.dumps(result))
