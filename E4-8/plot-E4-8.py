import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

#直线方程函数
def f_1(x, A, B):
    return  A*x+B
#二次曲线方程
def f_2(x,A,B,C):
	return A*x*x+B*x+C


#三次曲线方程
def f_3(x, A, B, C, D):
    return A*x*x*x + B*x*x + C*x + D

def plotLine1(x_vars,y_vars1,y_vars2):
    #三次函数拟合与绘制
    A1,B1,C1,D1 = optimize.curve_fit(f_3, x_vars,y_vars1)[0]
    A2,B2,C2,D2 = optimize.curve_fit(f_3, x_vars,y_vars2)[0]
    x1 = np.arange(x_vars[0],x_vars[-1] , 0.01)
    x2 = np.arange(x_vars[0],x_vars[-1],0.01)
    y1 = A1*x1*x1*x1 + B1*x2*x1 + C1*x1 + D1
    y2 = A2*x2*x2*x2 + B2*x2*x2 + C2*x2 + D2
    #y_vars = y_vars1.copy()
    #y_vars.extend(y_vars2)
    #绘制散点
    l01 = plt.scatter(x_vars, y_vars1, 25, "red")
    l02 = plt.scatter(x_vars, y_vars2, 25, "yellow")
    l1, = plt.plot(x1, y1, "blue")
    l2, = plt.plot(x2, y2, "green")
    plt.xticks(x_vars)
    plt.yticks(y_vars1,rotation=0)
    plt.xlabel('z/cm')
    plt.ylabel('B/mT')
    #plt.title("B和z关系曲线(拟合曲线)")
    plt.legend(handles = [l01,l1,l02,l2,], labels = ['测量值','测量值','理论值 ','理论值 '], loc = 'best')
    plt.tight_layout()
    plt.grid()
   
    plt.show()

def plotLine2(x_vars,y_vars1,y_vars2,y_vars3,y_vars4):
    #三次函数拟合与绘制
    A1,B1,C1,D1 = optimize.curve_fit(f_3, x_vars,y_vars1)[0]
    A2,B2,C2,D2 = optimize.curve_fit(f_3, x_vars,y_vars2)[0]
    A3,B3,C3,D3 = optimize.curve_fit(f_3, x_vars,y_vars3)[0]
    A4,B4,C4,D4 = optimize.curve_fit(f_3, x_vars,y_vars4)[0]
    x1 = np.arange(x_vars[0],x_vars[-1] , 0.01)
    x2 = np.arange(x_vars[0],x_vars[-1],0.01)
    x3 = np.arange(x_vars[0],x_vars[-1],0.01)
    x4 = np.arange(x_vars[0],x_vars[-1],0.01)
    y1 = A1*x1*x1*x1 + B1*x2*x1 + C1*x1 + D1
    y2 = A2*x2*x2*x2 + B2*x2*x2 + C2*x2 + D2
    y3 = A3*x3*x3*x3 + B3*x3*x3 + C3*x3 + D3
    y4 = A4*x4*x4*x4 + B4*x4*x4 + C4*x4 + D4
    
    y_vars = y_vars1.copy()
    y_vars.append(min(y_vars3))
    j=1
    for i in range(5):
        y_vars.append(y_vars3[j])
        j+=3
    y_vars.append(max(y_vars3))
    y_vars.append(max(y_vars4))
    #绘制散点
    plt.figure(figsize=[15,15])
    l01 = plt.scatter(x_vars, y_vars1, 25, "red")
    l02 = plt.scatter(x_vars, y_vars2, 25, "green")
    l03 = plt.scatter(x_vars, y_vars3, 25, "blue")
    l04 = plt.scatter(x_vars, y_vars4, 25, "yellow")
    l1, = plt.plot(x1, y1, "red")
    l2, = plt.plot(x2, y2, "green")
    l3, = plt.plot(x3, y3, "blue")
    l4, = plt.plot(x4, y4, "yellow")
    plt.xticks(x_vars)
    plt.yticks(y_vars,rotation=0,fontsize=5)
    plt.xlabel('z/cm')
    plt.ylabel('B/mT')
    #plt.title("B和z关系曲线(拟合曲线)")
    plt.legend(handles = [l01,l1,l02,l2,l03,l3,l04,l4,], labels = ['Ba','Ba','Bb ','Bb','Ba_Bb','Ba_Bb','Ba_b','Ba_b'], loc = 'best')
    plt.tight_layout()
    plt.grid()
    
    plt.show()
	
    
	

    

def f_input1():
	y_var1 = list(input("测量值:").split(" "))
	y_var2 = list(input("理论值:").split(" "))
	y_vars1 = []
	y_vars2 = []
	for y1 in y_var1:
		if y1 == ' ':
			break
		y_vars1.append(float(y1))
	
	for y2 in y_var2:
		if y2 == ' ':
			break
		y_vars2.append(float(y2))
	return y_vars1,y_vars2

def f_input2():
	y_var1 = list(input("Ba:").split(" "))
	y_var2 = list(input("Bb:").split(" "))
	y_var3 = list(input("Ba_Bb:").split(" "))
	y_var4 = list(input("Ba_b:").split(" "))
	y_vars1 = []
	y_vars2 = []
	y_vars3 = []
	y_vars4 = []
	for y1 in y_var1:
		if y1 == ' ':
			break
		y_vars1.append(float(y1))
	
	for y2 in y_var2:
		if y2 == ' ':
			break
		y_vars2.append(float(y2))
	for y3 in y_var3:
		if y3 == ' ':
			break
		y_vars3.append(float(y3))
	
	for y4 in y_var4:
		if y4 == ' ':
			break
		y_vars4.append(float(y4))
	return y_vars1,y_vars2,y_vars3,y_vars4	


def main():
	x_vars = range(-9,10,1)
	while 1:
		select = input("请输入要绘制的图的数字（1,2,3分别代表图1,2,3）：")
		if select == '1':
			y_vars1,y_vars2 = f_input1()
			plotLine1(x_vars,y_vars1,y_vars2)
			break
		elif select=='2' or select=='3':
			y_vars1,y_vars2,y_vars3,y_vars4 = f_input2()
			plotLine2(x_vars,y_vars1,y_vars2,y_vars3,y_vars4)
			break
		else:
			print("请输入正确的数字！！\n")
	
	

	

main()

