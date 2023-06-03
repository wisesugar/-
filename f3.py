import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6), dpi=120)#设置画布
plt.rcParams['font.family'] = ['STZhongsong']
x=np.linspace(0,6,666)#x取值范围
y=np.cos(2*np.pi*x)*np.exp(-x)+0.8
z=0.5*np.cos(x**2)+0.8
plt.plot(x,y,color='b',linewidth=2,linestyle="-")
plt.scatter(x, z, c='g', s=10)#以点绘制
plt.fill_between(x, y, z, color='gray', alpha=0.4)#在曲线交汇处绘制阴影 alpha代表颜色深度
plt.text(4, 1.8, 'y=cos(2Πx)exp(-x)+0.8', fontsize=10,color='b')
plt.text(4, 1.75, 'z=0.5 cos(x2)+0.8', fontsize=10,color='g')   #显示俩图像解析式
plt.xlabel('时间(s)')
plt.ylabel('幅度(mV)')
plt.grid()#网格
plt.title('全局阴影曲线绘制')
plt.tight_layout()
plt.show()