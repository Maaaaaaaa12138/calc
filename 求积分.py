from math import *

def f(x):
    return pow(x-3*pow(x, 2)+2*pow(x, 3)+pow(e, x), 0.5)

def T2n(Tn, k):
    temp = 0
    for i in range(1, 2**(k-1) + 1):
        temp += f((2*i-1)*(2/(pow(2, k))))
    return (1/2) * Tn + ((2/(pow(2, k))) * temp)


tn = (1/2) * (f(0) + f(2))
t2n = T2n(tn, 2)
print("k    T2k")
print(f"{0:<5}{tn:.6f}")
k = 2
while fabs(t2n - tn) >= 3 * pow(10, -5):
    print(f"{k-1:<5}{t2n:.9f}")
    k += 1
    tn = t2n
    t2n = T2n(tn, k)

print(f"符合精度要求的解为T2^{k-2}=T{2**(k-2)}={tn:.9f}")
