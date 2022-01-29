import ssl
import requests
from bs4 import BeautifulSoup
import html

xml_file = open("part.xml", encoding="utf-8")
html = xml_file.read()
soup = BeautifulSoup(html,'html.parser')
for child in soup.descendants:
    if child.name == 'item':
        filename=(child.title.next.strip()+".mp3").replace(' ','_')
        filename=filename.replace('/','_')
        #print(filename)
        audio_link=child.enclosure['url']
        print(audio_link)
        r_audio=requests.get(audio_link)
        with open(filename, 'wb') as f:
            f.write(r_audio.content)


        # for title_child in child.title:
        #     print(title_child,title_child)
        #print(child.title)
