from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Album, Artist, Booking, Contact

def home_view(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    template = loader.get_template('store/index.html')
    context = {'albums':albums}
    return HttpResponse(template.render(context, request=request))

def listing_album_view(request):
    albums = Album.objects.filter(available=True)
    context = {
        'albums':albums
    }
    return HttpResponse(context)

def detail_album_view(request, album_id):
    album =Album.objects.get(pk =album_id)
    artists_name = "".join([artist.name for artist in album.artists.all()])
    context = {
        'album_title': album.title,
        'artist_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }
    return HttpResponse (context)

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
    title = "Results for the query %s"%query        
    context = {
        'albums' : albums,
        'title' : title
    }
    return HttpResponse(context)