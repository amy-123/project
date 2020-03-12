#！/usr/bin/env python
# -*-coding:utf-8
#Author:Amy

import os


'''封装获取文件地址'''
def filePath(fileDir='data',fileme='login.yaml'):
	"""

	:param fileDir: 目录
	:param fileme: 文件的名称
	"""
	return os.path.join(
		os.path.dirname(os.path.dirname(__file__)),fileDir,fileme)

'''封装写入文件'''
def writeContent(filename,content):
	with open(filePath(fileme=filename),'w') as f:
		f.write(str(content))

'''封装读取文件'''
def readContent(filename):
	with open(filePath(fileme=filename),'r') as f:
		return f.read()