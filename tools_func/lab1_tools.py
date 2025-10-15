import matplotlib.pyplot as plt
import numpy as np

def plot_complex_polygon(numbers, title="complex numbers"):
    """
    在阿根图上绘制复数列表，并将点按顺序连接起来。
    
    参数：
    numbers (list): 要绘制的复数列表
    title (str): 图表标题
    """
    # 提取实部和虚部
    real_parts = [z.real for z in numbers]
    imag_parts = [z.imag for z in numbers]
    
    # 创建图表
    plt.figure(figsize=(8, 8))
    
    # 绘制点之间的连线（前一个点到后一个点）
    plt.plot(real_parts, imag_parts, 'b-', alpha=0.4)  # 蓝色半透明连线
    
    # 绘制点（在连线上方显示）
    plt.scatter(real_parts, imag_parts, color='blue', zorder=5)
    
    # 添加标签和网格
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title(title)
    plt.grid(True)
    
    # 设置等比例并居中坐标轴
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # 基于数据设置界限
    max_val = max(max(np.abs(real_parts)), max(np.abs(imag_parts))) * 1.1
    plt.xlim(-max_val, max_val)
    plt.ylim(-max_val, max_val)
    
    plt.show()