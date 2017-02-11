# coding:utf-8
import getIP
import testIP
import time

if __name__ == '__main__':
	ct1=time.time()
	getIP.spider()  # 爬取ip信息
	testIP.testAll()  # 筛选有用的ip
	ct2=time.time()
	print 'all time cost:%s secs' %(ct2-ct1)