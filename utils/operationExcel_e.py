#！usr/bin/env python
# -*-coding:utf-8 -*-
#auther: Amy
import xlrd
from common.public import *
from utils.operationYaml import OperationYaml
import json

class ExcelVarles:
	caseID="caseID"
	caseModel="模块"
	caseName="接口名称"
	caseUrl="请求地址"
	casePre="前置条件"
	method="请求方法"
	paramsType="请求参数类型"
	params="请求参数"
	expect="期望结果"
	isRun="是否运行"
	headers="请求头"
	status_code="状态码"


#
# 	def getcaseID(self):
# 		return self.caseID
#
# 	def descrition(self):
# 		return self.des
#
# 	def getrul(self):
# 		return self.url
#
# 	def getmothod(self):
# 		return self.metjod
#
# 	def getdata(self):
# 		return self.data
#
# 	def getexpect(self):
# 		return self.expect

class OperationExcele():
	def getSheet(self):
		book=xlrd.open_workbook(filePath('data','books.xls'))
		return book.sheet_by_index(0)

	@property
	def getExcelData(self):
		datas=list()
		title=self.getSheet().row_values(0)

		for row in range(1,self.getSheet().nrows):
			row_values = self.getSheet().row_values(row)
			datas.append(dict(zip(title,row_values)))
		return datas

	def runs(self):
		'''获取可执行测试用例'''
		run_list=[]
		for item in self.getExcelData:
			isRun=item[ExcelVarles.isRun]
			if isRun=='y':
				run_list.append(item)
			else:pass
		return run_list

	def case_lists(self):
		'''获取excel所有的测试用例'''
		cases=list()
		for item in self.getExcelData:
			cases.append(item)
			return cases


	# def paramse(self):
	# 	'''排除请求参数为空'''
	# 	for item in self.runs():
	# 		parms=item[ExcelVarles.params]
	# 		print(parms)
	# 		if len(str(parms).strip())==0:
	# 			pass
	# 		elif len(str(parms).strip())>=0:
	# 			return parms

	def case_prev(self,casePrev):
		'''根据前置条件，找到相关测试用例
		:param casePrev: 前置测试条件
		'''
		for item in self.case_lists():
			if casePrev in item.values():
				return item
		return None

	def prevHeaders(self,prevResult):
		"""
		:param prevResult: 请求头替换的值
		循环所有的请求头，判断token是否在列表，如果在将token替换
		"""
		for item in self.runs():
			headers = item[ExcelVarles.headers]
			if '{token}' in headers:
				headers=str(headers).replace('{token}',prevResult)
				return json.loads(headers)




if __name__ == '__main__':
    obj=OperationExcele()
    # for item in obj.runs():
    #     print(item)

    # obj.paramse()
    print(obj.prevHeaders('token'))

    # for item in obj.getExcelData:
	#     print(item[ExcelVarles.params])


