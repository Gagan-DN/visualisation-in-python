import numpy as nu
import matplotlib.pyplot as plt
# FOR PLOT

#1  y=x^3 for x values ranging from -10 to 10
x=nu.array(range(-10,10))
y=nu.array(x**3)
plt.plot(x,y)
plt.show()

#2 sin(x) from 0-4pi green dashed line
import math
x=nu.array(range(0,721))
u=nu.radians(x)
y=nu.array(nu.sin(u))
plt.plot(x,y,color="g",linestyle="dashed")
plt.show()

#3 linear relationship "y=5x+2" for x between-5 and 5
x=nu.array(range(-5,6))
y=nu.array((5*x)+2)
plt.plot(x,y)
plt.grid()
plt.show()

#4 "y=e^x" and "y=e^(-x)" both on same graph and legend distingush them
#x=nu.array(nu.random.normal(0,120,30))
x=nu.array(range(-10,10))
y1=nu.array((math.e)**x)
y2=nu.array((math.e)**(-x))
plt.plot(x,y1)
plt.plot(x,y2)
plt.legend(["y=e^x","y=e^(-X)"])
plt.show()

