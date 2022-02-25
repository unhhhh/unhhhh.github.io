from youtube_scrape_utils import YoutubeScraper


scraper = YoutubeScraper("api_key.txt")
unhhhh_playlist_id = 'PLhgFEi9aNUb2BNrIEecCGXApgeX7Yjwz8'
lines = scraper.transcript_html_from_playlist(unhhhh_playlist_id)

with open("index.html", "w") as file1:
    file1.write(lines)
