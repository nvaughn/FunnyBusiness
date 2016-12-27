from urllib import urlopen
from BeautifulSoup import BeautifulSoup

text = urlopen('http://www.decenttv.tv/category/funny-business').read()
soup = BeautifulSoup(text)

episodes = set()
for header in soup('div'):
    links = header('a', 'reference')
    if not links: continue
    link = links[0]
    episodes.add('%s (%s)' % (episodes.string, link['href']))
    
print '\n'.join(sorted(episodes, key=lambda s: s.lower()))
