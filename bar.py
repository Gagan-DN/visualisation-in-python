import matplotlib.pyplot as plt
import numpy as np


x=np.array(["ram","ko","ki","alia","aliaf"])
y=np.array([440,34,65,76,45])
plt.bar(x,y)
plt.show()

plt.barh(x,y)
plt.show()


#histogram graph
x=np.random.normal(170,10,250)
plt.hist(x)
plt.show()


#pie chat
y=np.array([60,32,180,30,18])
mylables=["android","prime_OS","mac_OS","chrome_OS","others"]
myexplode=[0.1,0,0,0.1,0]
plt.pie(y,labels=mylables,explode=myexplode,startangle=90,shadow=True)
plt.legend()
plt.show()
