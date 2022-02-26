from youtube_scrape_utils import YoutubeScraper


scraper = YoutubeScraper("api_key.txt", cache_dir='./subtitles')
unhhhh_playlist_id = 'PLhgFEi9aNUb2BNrIEecCGXApgeX7Yjwz8'
body = scraper.transcript_html_from_playlist(unhhhh_playlist_id, sep='\n\t')
full_html = f"""\
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>UNHhhh Complete Transcript - Find your favorite quotes!</title>
    <base href="./">
	<link href="stylesheet.css" id="user_stylesheet" rel="stylesheet" type="text/css"/>
	<link rel="shortcut icon" href="pride.ico">
</head>
<body>
<p>Find and click on your favorite quote below to be taken to the exact timestamp of the quote!</p>
<p>Has this site been helpful to find your favorite quotes from The Dolls™️? If so, <a href="https://www.paypal.com/paypalme/unhhhhbot" class="donation">tip this homosexual a coffee</a> so we can <a href="https://youtu.be/aE03-a3on7A?t=14"><u>keep the lights on!</u></a></p>
<p>Check out more of the girls here: 
<a href="https://www.youtube.com/c/WOWPresents"><u>WOWPresents</u></a> |
<a href="https://trixiemattel.com/"><u>Trixie Mattel</u></a> |
<a href="https://welovekatya.com/"><u>Katya Zamolodchikova</u></a>
<p>

<p>Any feedback or suggestions? <a href="https://github.com/unhhhh/unhhhh.github.io"><u>Create an issue on Github</u></a>.</p>

<hr />

    {body}
</body>
</html>
"""

with open("index.html", "w") as file1:
    file1.write(full_html)
