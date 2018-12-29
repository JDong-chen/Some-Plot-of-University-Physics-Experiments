import matplotlib.pyplot as plt
#from scipy.interpolate import spline
import numpy as np
from scipy import optimize

#直线方程函数
def f_1(x, A, B):
    return  A*x+B
def plotLine(x_vars,y_vars,x_vars2,y_vars2):

    
 
    #直线拟合与绘制
    A1, B1 = optimize.curve_fit(f_1, x_vars,y_vars)[0]
    x1 = np.arange(0,x_vars[-1] , 0.01)
    y1 = A1*x1 + B1

    A2, B2 = optimize.curve_fit(f_1, x_vars2,y_vars2)[0]
    x2 = np.arange(0,x_vars2[-1] , 0.01)
    y2 = A2*x2 + B2

    plt.subplot(211)
    #绘制散点
    plt.scatter(x_vars, y_vars, 25, "red")
    plt.plot(x1, y1, "blue")
    plt.xticks(x_vars)
    plt.yticks(y_vars)
    plt.xlabel('Is/mA')
    plt.ylabel('Uh/mV')
    plt.title("霍尔电压Uh与工作电流Is关系曲线(拟合曲线)")
    plt.tight_layout()
    plt.grid()
    

    plt.subplot(212)
    #绘制散点
    plt.scatter(x_vars2, y_vars2, 25, "red")
    plt.plot(x2, y2, "blue")
    plt.xticks(x_vars2)
    plt.yticks(y_vars2)
    plt.xlabel('Im/mA')
    plt.ylabel('Uh/mV')
    plt.title("霍尔电压Uh与励磁电流Im关系曲线(拟合曲线)")
    plt.tight_layout()
    plt.grid()
    plt.show()
	
    
	
    """
	z1 = np.polyfit(x_vars, y_vars,10)
	p1 = np.poly1d(z1)
	y_vals=np.polyval(z1,x_vars)

	#Hzs_smooh= np.linspace(float(min(Hzs)),float(max(Hzs)),300)
	#Swings_smooth = spline(Hzs,Swings,Hzs_smooh)

	#plt.subplot(211)
	plt.plot(x_vars,y_vals)
	plt.plot(x_vars,y_vars,'x')
	plt.xticks(x_vars)
	plt.yticks(y_vars)
	plt.xlabel('Is/mA')
	plt.ylabel('Uh/mV')
	plt.title("霍尔电压Uh与工作电流Is的关系曲线(拟合曲线)")
	plt.grid()
	plt.tight_layout()

	#plt.subplot(211)
	
	plt.plot(Hzs,Swings,'o')
	plt.plot(Hzs_smooh,Swings_smooth,'r')
	plt.xticks(Hzs)
	plt.yticks(Swings,fontsize=7)
	plt.xlabel('f')
	plt.ylabel('A')
	plt.title("音叉频率-振幅曲线")
	"""
	#plt.tight_layout()
    

def f_input():
	x_var = list(input("I:").split(" "))
	y_var = list(input("Uh:").split(" "))
	x_vars = []
	y_vars = []
	Hzs = []
	for x in x_var:
		if x == ' ':
			break
		x_vars.append(float(x))
	
	for y in y_var:
		if y == ' ':
			break
		y_vars.append(float(y))
	return x_vars,y_vars
	


def main():
    x_vars1,y_vars1 = f_input()
    x_vars2,y_vars2 = f_input()
    plotLine(x_vars1,y_vars1,x_vars2,y_vars2)
	
	

	

main()

