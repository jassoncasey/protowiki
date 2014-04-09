from django.db import models
import json

# Create your models here.
class Protocol(models.Model):
  name = models.CharField(max_length=32, unique=True)
  layer = models.IntegerField()

  def __unicode__(self):
    return self.name

def json_protocols():
  return { "nodes" : [{ "name" : p.name } for p in Protocol.objects.all()] }

class Relation(models.Model):
  protocol = models.ForeignKey(Protocol, related_name="carries")
  payload = models.ForeignKey(Protocol, related_name="carried")

  def __unicode__(self):
    return '%s / %s' % (self.protocol.name, self.payload.name)

def json_relations():
  return [{ "source" : r.protocol, "target" : r.payload } for r in Relation.objects.all()]
