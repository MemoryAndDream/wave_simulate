# -*- coding: utf-8 -*-
"""
File Name：     one_dim_wave
Description :
Author :       meng_zhihao
mail :       312141830@qq.com
date：          2024/2/12
"""
import matplotlib.pyplot as plt
total_length = 1000
densities = [100 for i in range(total_length)]

speeds = [0 for i in range(total_length)]

for i in range(450,550):
    densities[i] = 0


for j in range(20):
    for t in range(20):
        for i in range(1,total_length-1,1):
            a = (densities[i+1] + densities[i-1]-2*densities[i])/2/10 # a是力除以质量 这是一维绳子模型，感觉有些问题。
            speeds[i]+=a
        for i in range(1,total_length-1,1):
            densities[i] += speeds[i]
            if densities[i]<=0:
                speeds[i] = -speeds[i]
                densities[i] = -densities[i]
    xs = [x for x in range(len(densities))]
    plt.plot(xs, densities)
    plt.show()


# 一个上升一个下降会形成一个中点，（中点是max和背景密度的均值）将波形减半

# 过高的不影响

# 过低的空洞也是减半扩散