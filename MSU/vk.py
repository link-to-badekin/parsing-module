
from bs4 import BeautifulSoup
import requests



#полная информация по новости
def getContent( href ):
	# запрос по ссылке новости 
	page = requests.get( href)
	soup = BeautifulSoup(page.text, "html.parser")
	# контент контейнер
	soup = soup.find( name = 'div', class_ = 'post')

	novelty = dict()
	
	text = soup.find(name = 'div', class_ = 'et_pb_text_inner')
	novelty['text'] = text
	
	video = soup.find(name = 'video')
	if video is not None:
		novelty['video'] = video.find('source').get('src')
	
	raw = soup.findAll('img')
	picture = []
	for img in raw:
		if img is not None:
			picture.append(img.get('src'))
	novelty['picture'] = picture
	
	return novelty

import sys
file = open( 'vkpost.txt', 'w')
url = 'https://vk.com/sevmsustudents'
page = requests.get(url)
if (page.status_code!=200):
	print('all badd %d', page.status_code)
	sys.exit()

dirtyNews = []
News = []
soup = BeautifulSoup(page.text, "html.parser")
soup = soup.findAll( name = "div", class_ = "wi_body")
for post in soup:
	dirtyNews.append(post)
	print(post,"\n\n\n\n\n\n")
file.write ( str(dirtyNews) )
"""
# отбор только последних новостей
for item in soup:
	if (item.find_parent(name ='div', class_ = "overwrap") is not None): 
		dirtyNews.append(item)
#сбор информации из новостей
for item in dirtyNews:
	novelty = dict()
	novelty['cover'] = item.img.get('src')
	novelty['data'] = item.find(name = "div", class_= "number").string+ '/' + item.find(name = "div", class_= "year").string
	novelty['title'] = item.find('h3').string
	novelty['href'] = item.find('a').get('href')
	News.append(novelty)
#информация со страниц новостей 
for item in News:
	 item['novelty'] =  getContent(item['href'])
for item in News:
	file.write(str(item)+"\n\n\n");
file.close()
print('done')
"""