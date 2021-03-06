#coding:utf-8
import xlrd
import os

work_path = os.path.abspath('.')
class OperaCaseExcel(object):

	def get_case_name(self):
		res = []
		# opear = OperationJson()
		excel_path = os.path.join(work_path,r'data_config\TestRecordExcel\test.xlsx')
		path = excel_path.replace('\\','/')
		test_record = xlrd.open_workbook(path)
		table = test_record.sheets()[0]
		#获取Excel的个数
		excel_acount = table.nrows
		# print(excel_acount)
		for i in range(1,excel_acount):
			if table.cell_value(i,0) == '是':
				#获取case_excel_name
				case_name = table.cell_value(i,1)
				json_name = table.cell_value(i,2)
				run_data = (case_name,json_name)
				res.append(run_data)
		return res

if __name__ == '__main__':
	o = OperaCaseExcel()
	o.get_case_name()
	# o.get_case_json_name()