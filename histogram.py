import numpy as np
import matplotlib.pyplot as plt

#FOR HISTOGRAME
#13 create histogram to show ages of group of people at party
x=np.random.normal(0,10,100)
plt.hist(x)
plt.xlabel("age group")
plt.ylabel("number of people")
plt.show()


#14 histogram to show distribution of daily hours
#  spent on homework by students
x=np.random.normal(0,1,500)
plt.hist(x,color="orange")
plt.xlabel("hours student spend")
plt.ylabel("no of students")
plt.show()

#15 histogram to represent frequency of set of random numbers
#  generated with a uniform distribution
x=np.random.normal(0,4,200)
plt.hist(x,color="g")
plt.xlabel("uniformaly distrimuted range")
plt.ylabel("frequency of random number")
plt.show()

#16 histogram to visualize distribution of scores on test out of 100
x=np.random.normal(0,20,300)
plt.hist(x,color="r")
plt.xlabel("scorees distribution")
plt.ylabel("number of students")
plt.show()
