import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://bongoflixbd.top/crichd/'

# Send a GET request to the website
response = requests.get(url)

# Parse the response content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize m3u8 link as None
m3u8_link = None

# Find the <video> tag and extract the 'src' attribute
video_tag = soup.find('video')
if video_tag and video_tag.get('src'):
    m3u8_link = video_tag['src']

# If the m3u8 link is found, write it to a .m3u file
if m3u8_link:
    with open('output.m3u', 'w') as file:
        file.write(m3u8_link)
else:
    print('M3U8 link not found!')