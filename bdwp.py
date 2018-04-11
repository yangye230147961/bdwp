import requests
from urllib import parse
'''
parse模块需单独导入，
不可通过urllib.parse.方法
直接调用
'''
#-------------------------------------------
def bdwp_jy(BAIDUID,BDUSS,path,timeout=3):
	'''
	功能:
	传入文件路径，转码解压
	
	参数:
	bdwp_jy(BAIDUID,BDUSS,path,timeout=3)
	
	注意:
	timeout为请求时长，超出时长为超时，默认时长3s
	
	模块:
	requests urllib.parse
	
	返回:
	无
	
	'''
	headers={'Cookie':'PANWEB=1;BAIDUID='+str(BAIDUID)+':FG=1; BDUSS='+str(BDUSS)+';','User-Agent':'netdisk;7.8.1;Red;android-android;4.3','Host':'pcs.baidu.com','Connection':'Keep-Alive','Accept-Encoding':'gzip'}
	src=parse.quote(path,'utf-8')
	#路径转码
	url='http://pcs.baidu.com/rest/2.0/pcs/file?method=unzipdownload&path='+str(src)+'&subpath=%2F&app_id=250528&devuid=875497020550968&user=1'
	try:
		requests.get(url=url,headers=headers,timeout=timeout)
		'''
		传入参数发送请求，超出timeout时间后抛出
		requests.exceptions.RequestException
		超时错误，用异常处理跳过超时继续执行
		'''
	except requests.exceptions.RequestException:
		print('请求以发送，若文件过大或有密码，可能解压失败')
		#成功跳出异常，打印信息，继续执行

#-------------------------------------------
