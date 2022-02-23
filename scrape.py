import io
import os
import pandas as pd

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.http import MediaIoBaseDownload

from youtube_transcript_api import YouTubeTranscriptApi



scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

from pyyoutube import Api

unhhhh_playlist_id = 'PLhgFEi9aNUb2BNrIEecCGXApgeX7Yjwz8'

with open("api_key.txt", "r+") as file:
    API_KEY = file.read()

# api = Api(api_key=API_KEY)
# playlist_items = api.get_playlist_items(playlist_id=unhhhh_playlist_id, count=None)
# video_ids = [video.snippet.resourceId.videoId for video in playlist_items.items]
# r = api.get_captions_by_video(video_id=video_ids[0])
video_ids = ['MV7GAQPoGDg']

# assigning srt variable with the list
# of dictonaries obtained by the get_transcript() function
srt = YouTubeTranscriptApi.get_transcript(video_ids[0])
#caption_ids = ['vogDAhsPB2VVqwwuhgiQqokOIcUDLxcNykcxYw3vODo=']

def scrape_video_id(id, output_file):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.captions().download(
        id=id,
        #tfmt='srt',
    )
    # TODO: For this request to work, you must replace "YOUR_FILE"
    #       with the location where the downloaded content should be written.
    fh = io.FileIO(output_file, "wb")

    download = MediaIoBaseDownload(fh, request)
    complete = False
    while not complete:
        status, complete = download.next_chunk()


for video_id in caption_ids:
    out_file = f'subtitles/{video_id}.srt'
    if not os.path.isfile(out_file):
        scrape_video_id(video_id, out_file)


