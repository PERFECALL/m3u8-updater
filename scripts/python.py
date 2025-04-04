import requests
from bs4 import BeautifulSoup

url = 'https://bongoflixbd.top/crichd/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

m3u8_link = None
video_tag = soup.find('video')
if video_tag and video_tag.get('src'):
    m3u8_link = video_tag['src']

if m3u8_link:
    with open('output.m3u', 'w') as file:
        file.write(m3u8_link)
else:
    print("M3U8 link not found!")
