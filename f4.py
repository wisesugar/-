import random
import matplotlib.pyplot as plt
plt.figure(dpi=120)
plt.rcParams['font.family'] = ['STZhongsong']#设置matplotlib的默认字体族为'STZhongsong'。
dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for i in range(1000):
    s=random.randint(1, 6)
    dict[s] += 1
print(dict)
plt.bar(range(1, 7), dict.values())
plt.xlabel('值')
plt.ylabel('出现次数')
plt.title('随机结果！')
plt.grid(axis='y')##添加网格
plt.ylim(0,200)
plt.show()
