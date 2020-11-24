import matplotlib.pyplot as plt
import numpy as np


def _figure_bar(fontsize, ticksize, ylabel, x, y, xticks, log=False):
    fig = plt.figure()
    ax = plt.subplot(111)
    # font = {'family': 'Microsoft JhengHei', 'weight': 'bold', 'size': fontsize}  # noqa: E501
    # plt.rc('font', **font)

    # 设置右边和上边的框不显示
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # zorder设置优先级,数字越小越先画
    plt.bar(x=x, height=y, width=0.6, log=log, zorder=10)

    plt.ylabel(ylabel, fontsize=fontsize, fontweight='bold')
    plt.xticks(np.arange(len(xticks)),
               xticks,
               fontsize=ticksize,
               fontweight='bold')
    plt.yticks(fontsize=ticksize, fontweight='bold')
    # 不显示刻度线
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.set_xlim(-1, )
    # 显示横向的网格
    plt.grid(axis='y', zorder=1)
    # 标签尾与刻度对齐并旋转45度
    fig.autofmt_xdate(rotation=45)
    fig.tight_layout()
    plt.show()
