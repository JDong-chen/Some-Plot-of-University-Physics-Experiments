import matplotlib.pyplot as plt
from scipy.interpolate import spline
import numpy as np
from scipy import optimize


def plotLine(x_vars1,x_vars2,y_vars):

   


	x_vars1_smooh= np.linspace(min(x_vars1),max(x_vars1),300)
	y_vars_smooth = spline(x_vars1,y_vars,x_vars1_smooh)
	
	x_vars2_smooh= np.linspace(min(x_vars2),max(x_vars2),300)
	y_vars2_smooth = spline(x_vars2,x_vars1,x_vars2_smooh)
	
	plt.figure(figsize=[10,10])
	plt.subplot(211)
	plt.plot(x_vars1_smooh,y_vars_smooth)
	plt.plot(x_vars1,y_vars,'x')
	plt.xticks(x_vars1)
	plt.yticks(y_vars,fontsize=8)
	plt.xlabel('t/℃')
	plt.ylabel('Ig/uA')
	#plt.title("t-Ig曲线")
	plt.grid()
	plt.tight_layout()

	plt.subplot(212)
	plt.plot(x_vars2,x_vars1)
	plt.plot(x_vars2,x_vars1,'x')
	plt.xticks(x_vars2)
	plt.yticks(x_vars1,fontsize=8)
	plt.xlabel('Rt/kΩ')
	plt.ylabel('t/℃')
	#plt.title("Rt-t曲线")
	plt.grid()
	plt.tight_layout()
	plt.show()
	

def f_input():
	x_var = list(input("t:").split(" "))
	y_var = list(input("Ig:").split(" "))
	x_var2 = list(input("Rt:").split(" "))
	x_vars = []
	x_vars2 = []
	y_vars = []
	

	

	for x in x_var:
		if x == ' ':
			break
		x_vars.append(float(x))
	
	for y in y_var:
		if y == ' ':
			break
		y_vars.append(float(y))

	for x in x_var2:
		if x == ' ':
			break
		x_vars2.append(float(x))
	return x_vars,x_vars2,y_vars
	


def main():
    x_vars1,x_vars2,y_vars = f_input()
    plotLine(x_vars1,x_vars2,y_vars)
	
	

	

main()

