from pyyoutube import Api
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled

unhhhh_playlist_id = 'PLhgFEi9aNUb2BNrIEecCGXApgeX7Yjwz8'

with open("api_key.txt", "r+") as file:
    API_KEY = file.read()

api = Api(api_key=API_KEY)
playlist_items = api.get_playlist_items(playlist_id=unhhhh_playlist_id, count=None)


def srt_to_link(video_id, text, start):
    return f'<a href="https://youtu.be/{video_id}?t={int(start)}">{text}</a><br>\n'


all_lines = []
for i, video in enumerate(playlist_items.items):
    print(f"Scraping video {i+1}/{len(playlist_items.items)}...", end='\r')
    this_video_id = video.snippet.resourceId.videoId
    these_lines = [f'<h1>{video.snippet.title}</h1>\n']
    try:
        srt = YouTubeTranscriptApi.get_transcript(this_video_id)
    except TranscriptsDisabled as e:
        continue
    these_lines.extend(srt_to_link(this_video_id, _srt['text'], _srt['start']) for _srt in srt)
    all_lines.extend(these_lines)
    with open("index.html", "w") as file1:
        file1.writelines(all_lines)
