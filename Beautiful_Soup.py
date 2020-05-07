# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# text = urlopen('http://www.python.org/jobs').read()
# soup = BeautifulSoup(text,'html.parser')
# jobs =set()
# for job in soup.body.section('h2'):
#     jobs.add('{}({})'.format(job.a.string,job.a['href']))
# print ('\n'.join(sorted(jobs,key=str.lower)))


'''
采用beautifulsoup爬取猫眼电影的数据
'''
from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'

}
response = requests.get('https://maoyan.com/board/4',headers=headers)
print(response.text)
neirong=response.text
soup=BeautifulSoup(neirong,'lxml')
nr=soup.find_all(name='dd')
for dy in nr:
    print(dy.i.string)
    print(dy.a['title'])
    tupian=dy.find_all(name='img')
    print(tupian[1]['data-src'])
    print(dy.find_all(class_="star")[0].string)
    print(dy.find_all(name='i')[1].string,dy.find_all(name='i')[2].string)