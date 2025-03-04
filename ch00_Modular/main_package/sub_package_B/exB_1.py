# import main_package.sub_package_A.exA_1 as exA1   # 絕對路徑
# from main_package.sub_package_A import exA_1 as exA1
from ..sub_package_A import exA_1 as exA1   # 相對路徑寫法  不可以用import開頭 一定要用from
exA1.hello()

def hello():
	print("exB_1")