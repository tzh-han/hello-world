#从电脑里面加载下面这些工具 模块
import pandas
import seaborn
import matplotlib.pyplot
import statsmodels.api

#使用工具！
data = pandas.read(r'C:\Users\Lenovo\Desktop\aa46323cf301303f0b12de6dee17689d_7d68e5d721d4a7c60b19b892b9379cae_8.csv')

#使用seaborn模块绘制这些数据的散点图
seaborn.lmplot(x='years',y='salary',data=data)

#使用matplotlib.pyplot模块显示画面
matplotlib.pyplot.show()

#使用statsmodels.api计算回归线：
fit = statsmodels.api.formuls.ols('salary~years',data= data).fit()
print(fit.params)