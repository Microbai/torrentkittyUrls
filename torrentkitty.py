#!/usr/bin/python
# -*- coding: UTF-8 -*- 
 
import re
import cfscrape
scraper = cfscrape.create_scraper()
pattern = re.compile(r'(<div class="pagination">)(.*?)(</div>)',re.M)
urls = ""
key = "eyan"
text = str(scraper.get("https://www.torrentkitty.tv/search/" + key + "/" + str(1)).content)
m = pattern.findall(text)
pattern = re.compile(r'\d+',re.M)
m = pattern.findall(m[0][1])
page = m[-3]
pattern = re.compile(r'(magnet:\?xt=.*?)(")',re.M)
for num in range(1,int(page)) :
    text = str(scraper.get("https://www.torrentkitty.tv/search/" + key + "/" + str(num)).content)
    m = pattern.findall(text)
    for v in m :
        urls = urls + v[0] + "\n"

# 打开一个文件
fo = open("foo.txt", "w")
fo.write(urls)
# 关闭打开的文件
fo.close()