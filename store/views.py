# from django.shortcuts import render
from email import message
from django.http import HttpResponse

from store.models import ALBUMS

def listing_album_view(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)
