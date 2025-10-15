import matplotlib.pyplot as plt
import numpy as np


def plot_complex_polygon(numbers, title="Complex Polygon", color='blue'):
    """
    在阿根图上绘制复数多边形，将点按顺序连接起来。
    
    参数：
    numbers (list): 复数顶点列表
    title (str): 图表标题
    color (str): 多边形边线和顶点的颜色
    """
    # 提取实部和虚部
    real_parts = [z.real for z in numbers]
    imag_parts = [z.imag for z in numbers]
    
    # 添加第一个点作为终点以闭合多边形
    if len(numbers) > 1:
        real_parts.append(numbers[0].real)
        imag_parts.append(numbers[0].imag)
    
    # 创建图表
    plt.figure(figsize=(8, 8))
    
    # 绘制多边形边线
    plt.plot(real_parts, imag_parts, color=color, linewidth=2, alpha=0.7)
    
    # 绘制顶点
    plt.scatter(real_parts[:len(numbers)], imag_parts[:len(numbers)], 
                color=color, s=80, zorder=5)
    
    # 添加标签和网格
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title(title)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # 设置等比例并居中坐标轴
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # 基于数据设置界限
    max_val = max(max(np.abs(real_parts)), max(np.abs(imag_parts))) * 1.1
    plt.xlim(-max_val, max_val)
    plt.ylim(-max_val, max_val)
    
    plt.show()