#！usr/bin/env python
# -*-coding:utf-8 -*-
#auther: Amy

from base.method import Requests
from utils.operationExcel_e import *
import pytest
import json
from common import *
import allure

excel=OperationExcele()
obj=Requests()

@pytest.mark.parametrize('datas',excel.runs())
def test_login_book(datas):
	'''获取excel中的请求参数并做序列化'''
	param=datas[ExcelVarles.params]
	if len(str(param).strip()) == 0:pass
	elif len(str(param).strip()) >= 0:
		param = json.loads(param)

	'''获取excel中的请求头并做序列化'''
	# header = datas[ExcelVarles.headers]
	# if len(str(header).strip()) == 0:pass
	# elif len(str(header).strip()) >= 0:
	# 	header = json.loads(header)

	'''
	1、获取有前置条件的测试用例login
	2、执行前置条件测试用例，获取结果信息token
	3、将获取的token替换需执行用例的请求参数
	4、执行测试用例
	'''
	#执行前置条件关联测试用例登录
	r=obj.post(url=excel.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.caseUrl],
	           json=json.loads(excel.case_prev(datas[ExcelVarles.casePre])[ExcelVarles.params]))
	precResult=r.json()['access_token']
	head = excel.prevHeaders(precResult)

	staus_codee = int(datas[ExcelVarles.status_code])

	def case_assert_result(r):
		assert r.status_code == staus_codee
		assert datas[ExcelVarles.expect] in json.dumps(r.json(),ensure_ascii=False)

	if datas[ExcelVarles.method]=='get':
		if '/books' in datas[ExcelVarles.caseUrl]:
			r=obj.get(url=datas[ExcelVarles.caseUrl],headers=head)
			case_assert_result(r=r)
		else:
			url=str(datas[ExcelVarles.caseUrl]).replace('{bookID}',readContent('bookid'))
			r=obj.get(url=url,headers=head)
			case_assert_result(r=r)

	elif datas[ExcelVarles.method]=='post':
		r=obj.post(url=datas[ExcelVarles.caseUrl],json=param,headers=head)
		writeContent(filename='bookid',content=str(r.json()[0]['datas']['id']))
		case_assert_result(r=r)

	elif datas[ExcelVarles.method]== 'delete':
		url=str(datas[ExcelVarles.caseUrl]).replace('{bookID}',readContent('bookid'))
		r=obj.delete(url=url,headers=head)
		case_assert_result(r=r)

	elif datas[ExcelVarles.method] =='put':
		url = str(datas[ExcelVarles.caseUrl]).replace('{bookID}', readContent('bookid'))
		r=obj.put(url=url,json=param,headers=head)
		case_assert_result(r=r)



if __name__ == '__main__':
    pytest.main(["-v","-s","test_login_token_book.py","--alluredir","./report"])
    import subprocess
    subprocess.call('allure generate report/ -o report/html --clean',shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p 8088 report/html',shell=True)


