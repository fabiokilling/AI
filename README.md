# AI
问一个姑娘她是前端还是后端，她说她是做AI的，我百度了下什么是做AI的，好像。。


到现在还没弄清楚，是不是太笼统了，是人工智能？


人工智能也分强人工智能和弱人工智能吧？


还有神经网络是不是呢？


或者机器学习？

Optimization for Data Science(数据科学的优化)

Advanced Learning For Text and Graph Data(针对文本和图形数据的高级学习)

Data Camp(数据营)

Structured Data : Learning and Prediction(结构化数据：学习和预测)

在Python中实现推荐系统需要用到的数据集存在Git项目的Files文件夹里，名为ml-100k

(出现DeprecationWarning的解决办法可参考DeprecationWarning.py)

报错信息：

DeprecationWarning: 

This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved.

Also note that the interface of the new CV iterators are different from that of this module.

This module will be removed in 0.20.

分析：

cross_validation模块被弃用了，改为支持model_selection这个模块

解决方法：

from sklearn import cross_validation as cv

train_data, test_data = cv.train_test_split(df, test_size=0.25)

改为

from sklearn.model_selection import train_test_split

train_data, test_data = train_test_split(df, test_size=0.25)
