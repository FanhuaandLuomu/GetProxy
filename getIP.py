# coding:utf-8
# 爬取ip代理程序 每次运行将爬取代理网站的前三页

import requests
import urllib2
import random
import time
from scrapy import Selector
from bs4 import BeautifulSoup

User_Agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0']
headers = {}
headers['User-Agent'] = User_Agent[0]

def getHeaders(AgentList):
	headers={'User_Agent':random.choice(AgentList)}
	return headers

def getOnePageIP(url,pageNo):
	curl=url+pageNo
	print 'start spider %s page of ips' %pageNo
	# headers=getHeaders(User_Agent)
	# print headers
	# html=requests.get(page_url,headers=headers).content
	req=urllib2.Request(curl,headers=headers)
	res=urllib2.urlopen(req)
	html=res.read()

	soup=BeautifulSoup(html,'lxml')
	trList=soup.findAll('tr')[1:]  # 第一个tr舍弃
	# time.sleep(2)
	# print html
	# cont=Selector(text=html).xpath(u'//*[@id="ip_list"]/tbody/tr[1]')
	# trList=cont.xpath(u'//td')
	# print len(trList)
	# print cont
	print len(trList)
	infoList=[]
	for item in trList:
		# print item
		tdList=item.findAll('td')
		ip=tdList[1].contents[0].strip()
		port=tdList[2].contents[0].strip()

		address=tdList[4].get_text().strip()  # get_text() 得到所有的文本
		ipType=tdList[6].contents[0].strip()
		date=tdList[-1].contents[0].strip()
		print ip,port,address,ipType,date

		line=ip+'\t'+port+'\t'+address.encode('utf-8').decode('utf-8')+'\t'+ipType+'\t'+date
		infoList.append(line)
	print '%s page of ips (has %d ips) spider success!' %(pageNo,len(infoList))
	# write2File('ip_list.txt',infoList)  # 将结果写入文件
	return infoList

def write2File(filename,textList):
	f=open(filename,'w')
	if len(textList)>0:
		lines='\n'.join(textList)
		f.write(lines.encode('utf-8'))
	f.close()

def spider():
	t1=time.time()
	filename='ip_list.txt'
	url = 'http://www.xicidaili.com/nn/'
	pageNum=3  # 爬取前三页
	infoList=[]
	for pageNo in range(1,pageNum+1):
		infoList+=getOnePageIP(url,str(pageNo))  # 爬取一页
	print '%d pages spider all success,all %d ips...' %(pageNum,len(infoList))
	write2File(filename,infoList) # 将结果写入文件
	t2=time.time()
	print('get ip time cost:%s secs' %(t2-t1))

# if __name__ == '__main__':
# 	# headers=getHeaders(User_Agent)  # 得到一个随机浏览器头
# 	# spider()
# 	getOnePageIP('http://www.xicidaili.com/nn/','1')
	
