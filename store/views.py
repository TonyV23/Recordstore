# from django.shortcuts import render
from django.http import HttpResponse

from .models import Album, Artist, Booking, Contact

def home_view(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    return HttpResponse(message)

def listing_album_view(request):
    albums = Album.objects.filter(available=True)
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    return HttpResponse(message)

def detail_album_view(request, album_id):
    album =Album.objects.get(pk =album_id)
    artists = "".join([artist.name for artist in album.artists.all()])
    message = " Le nom de l'album est {} . il a été ecrit par {} ".format(album.title, artists)
    return HttpResponse (message)

def search_album_view(request):
    query = request.GET.get('query')
    if not query :
        albums = Album.objects.all()
    else :
        albums = Album.objects.filter(title__icontains=query)
        
        if not albums.exists():
            albums = Album.objects.filter(artists__name__icontains=query)
        
        if not albums.exists():
            message = "Y a R Viper23"
        
        else :
            albums = ["<li>{}</li>".format(album.title) for album in albums]
            message = """
                Les resultats de votre recherche :
                    <ul>{}</ul>
            """.format("<li></li>".join(albums))
    return HttpResponse(message)