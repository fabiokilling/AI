以下两条命令是困扰无数人的关于Spyder绘图问题的

%matplotlib qt5

%matplotlib inline


以下是matplotlib绘图汉字为方块的解决方法

import matplotlib.pyplot as plt

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体

mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

如果解决了您的问题，请帮忙打赏作者

支付宝账号为243202504@qq.com
