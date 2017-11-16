from bs4 import BeautifulSoup
import pickle
import requests

url = 'https://www.discogs.com/label/801577-Cruisin-Classics'

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content)
table = soup.find(id='label')
titles = table.findAll(class_='title')
title_links = map(lambda t: t.find('a')['href'], titles)[1:]

base_url = "https://www.discogs.com"
result = []
for link in title_links:
	url = base_url + link
	album_request = requests.get(url, headers=headers)
	soup = BeautifulSoup(album_request.content)
	tracklist = soup.findAll(class_='tracklist_track')
	for track in tracklist:
		artist = track.find(class_='tracklist_track_artists').find('a').text
		track_title = track.find('span', class_='tracklist_track_title').text
		result.append({'artist':artist, 'track_title':track_title})

with open('cruisin_classics_songlist.pickle','wb') as handle:
		pickle.dump(result, handle)
