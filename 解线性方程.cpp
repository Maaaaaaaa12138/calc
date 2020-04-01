#include<iostream>
#include<cstdlib>
#include<string>
#include <iomanip>
#include<cmath>
using namespace std;
// 定义常量e
double const M_E = 2.7182818284590452353602874713527;

// 原函数Fx
double f(double x){
	return pow(M_E, x) + 3 * pow(x, 3) - 2 * pow(x, 2) + x - 2;
}

// 导函数
double fp(double x){
	return pow(M_E, x) + 9 * pow(x, 2) - 4 * x + 1;
}

// 牛顿迭代法Gx函数
double gN(double xk){
	return xk - (f(xk) / fp(xk));
}

// 弦割法Gx函数
double gX(double x1, double x0){
	return x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0));
}

// 弦割法求近似解, eps为精度
void XG(double x0, double x1, double eps){
	int index = 1;
	double temp;
	cout << "count" << '\t' << "Xk-1" << "\t\t" << "Xk" << endl;
	cout << index << '\t' << x0 << "\t\t" << x1 << endl;
	// 控制精度和最大迭代次数
	while (fabs(x0 - x1) >= eps && index <= 40)
	{
		index++;
		temp = 	x1;
		x1 = gX(x1, x0);
		x0 = temp;
		cout  << index << '\t' << x0 << "\t\t" << x1 << endl;
	}
	// 输出结果
	cout << "The solution satisfying the accuracy requirement is: x" << index << "=" << x1 << endl;
}


// 牛顿法求解方程组
void N(double x0, double eps){
	int index = 0;
	// 初始化xk-1, 避免第一步就跳出
	double xk, xk_1=x0+eps * 100;
	xk = x0;
	cout << "count" << '\t' << "Xk" << endl;
	cout << index << '\t' << xk << endl;
	while ( fabs(xk - xk_1) >= eps && index <= 40 )
	{
		index++;
		xk_1 = xk;
		xk = gN(xk_1);
		cout << index << '\t' << xk << endl;
	}
	// 输出结果
	cout << "The solution satisfying the accuracy requirement is: x" << index << "=" << xk << endl;
}


int main()
{
	cout << "String cut method:\n" << endl;
	XG(0.5, 0.4, pow(10,-4));
	cout << setw(100) << setfill('-') << endl;
	cout << "\nNewton method:\n" << endl;
	N(0.7, pow(10, -5));
	// 暂停
	getchar();
	return 0;
}
