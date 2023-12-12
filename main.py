import pytest
import pathlib
import shutil
import os


SRC_PATH = pathlib.Path(__file__).parent

# pytest生成的allure数据
ALLURE_DIR = SRC_PATH / 'report/allure_data'
# allure报告导出目录
ALLURE_REPORT =  SRC_PATH / 'report/allure_report'
# 测试用例目录
testcast_dir =  SRC_PATH / 'testcases'

pytest.main(['-sv',testcast_dir,'--alluredir',ALLURE_DIR])
# environment.properties文件提供allure报告环境变量
shutil.copy(f"{SRC_PATH}/environment.properties",ALLURE_DIR)
os.system(f'allure generate {ALLURE_DIR} -o {ALLURE_REPORT} --clean')