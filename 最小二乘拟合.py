import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt

def f1(k, j):
    res = 0
    for i in range(m):
        res += f[k](x[i]) * f[j](x[i])
    return res

def f2(k):
    return sum([f[k](x[i]) * y[i] for i in range(m)])

# 获取系数矩阵
def getA():
    A = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(f1(i, j))
        A.append(temp)
    return A

# 获取常数列矩阵
def getB():
    B = []
    for i in range(n):
        B.append(f2(i))
    return B

def getfas(A, B):
    a = solve(np.mat(A), np.mat(B).T).T
    return [round(i, 2) for i in a.tolist()[0]]


m = 11
x = [1, 1.4, 1.8, 2.2, 2.6, 3, 3.4, 3.8, 4.2, 4.6, 5]
y = [4.7187, 9.4496, 13.3248, 16.0722, 17.4894, 17.5794, 16.6755, 15.6332, 16.0858, 20.8430, 34.4605]

n = 6
f = [lambda x: 1, lambda x: x, lambda x: pow(x, 2), lambda x: pow(x, 3), lambda x: pow(np.e, x), lambda x: np.log(x)]

def getRes():
    res = getfas(getA(), getB())
    print(f"拟合函数为：{res[0]}+{res[1]}x+{res[2]}x^2{res[3]}x^3+{res[4]}e^x+{res[5]}ln(x)")
    Gx = lambda x: sum([f[i](x) * res[i] for i in range(n)])
    return Gx

Gx = getRes()

# 将真实值点绘出来
plt.scatter(np.array(x), np.array(y), label="rel point")
# 绘制拟合函数
plt.plot(np.linspace(1, 5), np.array([Gx(i) for i in np.linspace(1, 5)]), 'r', label="fitting function")
plt.xlabel("x")
plt.ylabel("y")
plt.title("least square fit")
plt.legend()
plt.show()

