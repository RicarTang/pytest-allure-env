import pytest
import os


# pytest生成的allure数据
ALLURE_DIR = os.path.join(os.path.dirname(__file__),'./report/allure_data')
# allure报告导出目录
ALLURE_REPORT = os.path.join(os.path.dirname(__file__),'./report/allure_report')
# 测试用例目录
testcast_dir = os.path.join(os.path.dirname(__file__),'./testcases')

pytest.main(['-sv',testcast_dir,'--alluredir',ALLURE_DIR])
os.system(f'allure generate {ALLURE_DIR} -o {ALLURE_REPORT} --clean')