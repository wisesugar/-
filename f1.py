import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['STZhongsong']#设置matplotlib的默认字体族为'STZhongsong'。
x=np.linspace(0,11,451)
y=np.cos(2*np.pi*x)*np.exp(-x)
plt.plot(x,y,color='r',linewidth=2,linestyle="-")
plt.xlabel('芝士X轴')
plt.ylabel('芝士Y轴')
plt.savefig('plot.jpg', format='jpg')
plt.show()