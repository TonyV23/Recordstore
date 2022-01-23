# from django.shortcuts import render
from email import message
from django.http import HttpResponse

from store.models import ALBUMS

def listing_album_view(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)

def detail_album_view(request, album_id):
    id = int(album_id)
    album = ALBUMS [id]
    artists = " ".join([artist['name'] for artist in album ['artists']])
    message = " Le nom de l'album est {} . il a été ecrit par {} ".format(album['name'], artists)
    return HttpResponse (message)