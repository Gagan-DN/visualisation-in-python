import numpy as nu
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[20,40,60,80,100,120]
r=nu.array(x)
s=nu.array(y)
plt.plot(r,s)
plt.show()
plt.plot(r,s,"*")
plt.show()
x=nu.array([1,2,3,3,45,65,76])
y=nu.array([30,32,26,76,56,0,99])
plt.plot(x,y,marker="*",ms=10,mfc="g")
plt.plot(y,x,marker="*",ms=10,mfc="r")
plt.show()



#bar graph  
plt.bar(x,y)
plt.show()
