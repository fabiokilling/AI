报错信息：
DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved.
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
