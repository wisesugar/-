import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6), dpi=120)#设置画布
plt.rcParams['font.family'] = ['STZhongsong']#设置matplotlib的默认字体族为'STZhongsong'。

x=np.linspace(0,11,451)#x取值范围
y=np.cos(x**2)
z=np.sin(x*2)
q=np.tan(np.pi*2*x)##解析式
plt.plot(x,y,color='r',linewidth=1,linestyle="-")
plt.plot(x,z,color='b',linewidth=1,linestyle="-")
plt.plot(x,q,color='k',linewidth=2,linestyle="-")##折线参数
plt.xlabel('芝士X轴')
plt.ylabel('芝士Y轴')##给x、y轴添加标题
plt.grid()##添加网格
plt.ylim(-50, 50)##y轴的取值范围
plt.show()