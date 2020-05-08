import requests
import re
import time
headers = {

   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
}
pattern = re.compile('<dd>.*?"board-index board-index-.*?">(.*?)</i>.*?<img data-src="(.*?)".*?<p class="name">.*?">('
                     '.*?)</a></p>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<p '
                     'class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i>.*?</dd>',re.S)
for i in range(10):
   time.sleep(1)
   r = requests.get('https://maoyan.com/board/4?offset='+str(i*10),headers=headers)
   print(r.text)
   content = re.findall(pattern,r.text)
   for item in content:
      print('排名:'+str(item[0])+'\t'+'电影名 《'+item[2].strip()+'》'+'\t'+item[3].strip()+'\t'+item[4].strip()+'\t'+'评分：'+item[5].strip()+ item[6].strip()+'\n'+'图片：'+item[1]+'\n')
      with open('zxjmaoyan2.0.txt','a',encoding='utf-8') as f:
         f.write('排名:'+str(item[0])+'\t'+'电影名 《'+item[2].strip()+'》'+'\t'+item[3].strip()+'\t'+item[4].strip()+'\t'+'评分：'+item[5].strip()+ item[6].strip()+'\n'+'图片：'+item[1]+'\n')
