
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_sin(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * 0.5) * (7 - i) * flip)


plot_sin()
plt.show()



def plot_sin(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * 0.5) * (7 - i) * flip)


sns.set()
plot_sin()
plt.show()
sns.set()       # 使用默认设置
data = sns.load_dataset('flights')            # 加载sns自带数据集
data = data.pivot('month', 'year', 'passengers')
sns.heatmap(data, annot=True, fmt='d', lw=0.5, cmap="YlGnBu")
plt.show()