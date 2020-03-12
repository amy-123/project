#！/usr/bin/env python
# -*-coding:utf-8
#Author:Amy
import yaml
from common.public import filePath

class OperationYaml:

	'''yaml文件获取列表数据'''
	def readYaml(self):
		with open(filePath('data','login.yaml'),'r',encoding='utf-8') as f:
			return list(yaml.safe_load_all(f))

	'''yaml文件获取字典数据'''
	def dictYaml(self,fileDir='config',filename='books.yaml'):
		with open(filePath(fileDir=fileDir,fileme=filename),'r',encoding='utf-8') as f:
			return yaml.safe_load(f)


if __name__ == '__main__':
    obj=OperationYaml()
    print(obj.dictYaml('config','books.yaml'))