#coding: utf-8
"""
Created on Mon Apr 16 15:36:33 2018

@author: ArcherX
"""
from aip import AipFace
# 定义常量 
# 下面这三个值推荐自己去百度的SDK官网去登陆自己账号创建应用，生成自己的账号
# http://ai.baidu.com/tech/face 
APP_ID = '9851066'  
API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'  
SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'  
  
# 初始化AipFace对象  
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)  
  
# 读取图片  
filePath = ""    # 在这里输入图片名，图片文件注意保存在同一路径  
def get_file_content(filePath):  
    with open(filePath, 'rb') as fp:  
        return fp.read()  
  
# 定义参数变量  
options = {  
    'max_face_num': 1,  
    'face_fields': "age,beauty,expression,faceshape",  
}  
# 调用人脸属性检测接口  
result = aipFace.detect(get_file_content(filePath),options)  
  
print(result)  
print(type(result))  
