import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_album_cover_url(CLIENT_ID, CLIENT_SECRET, album_id):
  client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
  sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

  id = "spotify:album:" + album_id

  results = sp.album(id)
  album_cover_url = results["images"][0]["url"]

  return album_cover_url