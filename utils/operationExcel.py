#！usr/bin/env python
# -*-coding:utf-8 -*-
#auther: Amy

import xlrd
from common.public import *
from utils.operationYaml import OperationYaml

class ExcelVarles:
	caseID=0
	des=1
	url=2
	metjod=3
	data=4
	expect=5

	def getcaseID(self):
		return self.caseID

	def descrition(self):
		return self.des

	def getrul(self):
		return self.url

	def getmothod(self):
		return self.metjod

	def getdata(self):
		return self.data

	def getexpect(self):
		return self.expect

class OperationExcel(OperationYaml):
	def getSheet(self):
		book=xlrd.open_workbook(filePath('data','books.xls'))
		return book.sheet_by_index(0)

	@property
	def getRows(self):
		'''获取总行数'''
		return self.getSheet().nrows

	@property
	def getCols(self):
		'''获取总列数'''
		return self.getSheet().ncols

	def getValue(self,row,clo):
		return self.getSheet().cell_value(row,clo)

		'''获取caseid'''
	def getCaseID(self,row):
		return self.getValue(row=row,clo=ExcelVarles().getcaseID())

	def geturl(self,row):
		url=self.getValue(row=row,clo=ExcelVarles().getrul())
		if '{bookID}' in url:
			url=str(url).replace({'bookID'},readContent('bookid'))
		else:
			return url

	def getMethod(self,row):
		return self.getValue(row=row,clo=ExcelVarles().getmothod())

	'''获取data列相关单元格的值'''
	def getData(self,row):
		return self.getValue(row=row,clo=ExcelVarles().getdata())

	'''将data列某个单元格的值与yaml文件的key映射，取出yaml文件中的请求参数'''
	def getjson(self,row):
		return self.dictYaml()[self.getData(row=row)]

	def getExpect(self,row):
		return self.getValue(row=row,clo=ExcelVarles().getexpect())



#
if __name__ == '__main__':
    obj=OperationExcel()
    print(obj.getExpect(1))
# #     print(obj.getCaseID(0))
#     print(obj.geturl(1))
#     print(obj.getData(0))
#     print(obj.getMethod(0))
#     print(obj.getjson(2))



