import requests
from bs4 import BeautifulSoup

fantasy_football_sites = []
fantasy_football_sites.append('https://bleacherreport.com/fantasy-football')
fantasy_football_sites.append('http://www.espn.com/fantasy/football/')
#fantasy_football_sites.append()
#fantasy_football_sites.append()
#fantasy_football_sites.append()


page = requests.get('http://www.espn.com/fantasy/football/')
soup = BeautifulSoup(page.content, 'html.parser')

tag_player = (input('Enter A Player: ')).title() #player search in Headding Tags
link_player = tag_player.lower().replace(' ','-') #player search in hfef tags
print(tag_player)
print(link_player)
#print(soup.prettify())

#print([type(item) for item in list(soup.children)])

#html = list(soup.children)[1]
#print(list(html.children))
possible_links = soup.find_all('a')
h3_headers = soup.find_all('h3')
h1_headers = soup.find_all('h1')

websites = set([])

#h3_hedders = list(soup.find_all('a'))
#print('World' in h3_hedders[3].get_text())

for link in possible_links:
    if(link.has_attr('href')) and link_player in link.attrs['href']:
        #print(type(link))
        websites.add((link.attrs['href']))


links_with_text = []
for a in soup.find_all('a', href=True):
    if tag_player in a.text:
        print(type(a))
        links_with_text.append(a['href'])


print(links_with_text)

#for text in h1_headers:
#    if(tag_player in text.get_text()):
#        #print(type(text))
#        print(type(text))
