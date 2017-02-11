# coding:utf-8
# 测试ip_list.txt 里面的ip代理是否可用
# 并将可用的ip代理写入可用文件
import urllib
import socket

socket.setdefaulttimeout(5)

def testOneIP(proxy,url):
	print 'now proxy:%s' %proxy
	try:
		res=urllib.urlopen(url,proxies=proxy).read()
		print res.decode('utf-8'),'this proxy:%s useful' %(proxy)
		return 1
	except Exception,e:
		print e
		return 0

def write2File(filename,line):
	f=open(filename,'a')
	f.write(line+'\n')
	f.close()

def testAll():
	url="http://ip.chinaz.com/getip.aspx"
	f=open('ip_list.txt','r')
	for line in f:
		pieces=line.strip().split('\t')
		ip=pieces[0]
		port=pieces[1]
		address=pieces[2]
		ipType=pieces[3]
		date=pieces[4]

		proxy_host='http://'+ip+':'+port
		proxy={'http':proxy_host}  # 代理ip
		useful=testOneIP(proxy,url)
		if useful:
			line=str(proxy)
			write2File('useful_ip.txt',line) # 将有用的ip写入文件

# if __name__ == '__main__':
# 	testAll()
url='http://ip.chinaz.com/getip.aspx'
proxy={'http': 'http://115.159.148.153:80'}
testOneIP(proxy,url)