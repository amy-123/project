#！usr/bin/env python
# -*-coding:utf-8 -*-
#auther: Amy

from base.method import Requests
from utils.operationYaml import OperationYaml
from utils.operationExcel import OperationExcel
import pytest
from common.public import *

class TestBook:
	obj=Requests()
	excel=OperationExcel()

	def assert_status_code(self,row,r):
		assert int(self.excel.getExpect(row=row)) is r.status_code

	def test_book_001(self):
		'''获取所有书籍的信息'''
		r=self.obj.get(url=self.excel.geturl(row=1))
		self.assert_status_code(row=1,r=r)

	def test_book_002(self):
		'''添加书籍'''
		r=self.obj.post(url=self.excel.geturl(2),json=self.excel.getjson(2))
		writeContent('bookid',r.json()[0]['datas']['id'])
		# writeContent('bookid', 1)
		self.assert_status_code(row=2,r=r)

	def test_book_003(self):
		'''查看书籍'''
		r=self.obj.get(url=self.excel.geturl(3))
		# print(readContent('bookid'))
		self.assert_status_code(row=3,r=r)


if __name__ == '__main__':
    pytest.main(["-v","-s","test_books.py::TestBook::test_book_003"])