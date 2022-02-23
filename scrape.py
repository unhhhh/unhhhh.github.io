from pyyoutube import Api

unhhhh_playlist_id = 'PLhgFEi9aNUb2BNrIEecCGXApgeX7Yjwz8'

with open("api_key.txt", "r+") as file:
    api_key = file.read()

api = Api(api_key=api_key)
playlist_items = api.get_playlist_items(playlist_id=unhhhh_playlist_id, count=None)
for video in playlist_items.items:
    this_video_id = video.snippet.resourceId.videoId
    r = api.get_captions_by_video(video_id=this_video_id)

    x = 2
