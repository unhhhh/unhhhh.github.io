from youtube_scrape_utils import YoutubeScraper


scraper = YoutubeScraper("api_key.txt")
unhhhh_playlist_id = 'PLhgFEi9aNUb2BNrIEecCGXApgeX7Yjwz8'
body = scraper.transcript_html_from_playlist(unhhhh_playlist_id)
full_html = f"""\
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>UNHhhh Complete Transcript - Find your favorite quotes!</title>
    <base href="./">
	<link href="stylesheet.css" id="user_stylesheet" rel="stylesheet" type="text/css"/>
	<link rel="shortcut icon" href="img/head_icon.ico">
</head>
<body>
{body}
</body>
</html>
"""

with open("index.html", "w") as file1:
    file1.write(full_html)
