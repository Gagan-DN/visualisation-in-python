import numpy as np
import matplotlib.pyplot as plt


#FOR BAR GRAPH

#5 bar graph to show number of students
#enrolled in 5 different courses labeled A-E

student=["A","B","C","D","E"]
enrolled=[123,43,56,340,236]
x=np.array(student)
y=np.array(enrolled)
plt.bar(x,y,color="orange")
plt.xlabel("cources")
plt.ylabel("number of enrolled")
plt.show()

#6 bar graph x_axis(months) y_axis(avg temprature of each month)
months=["JAN","FEB","MAR","APR","MAY","JUN","JULY","AUG","SEP","OCT","NOV","DEC"]
temprature=[20.5,22.7,25.2,27.1,26.7,24.2,23.0,23.0,23.1,22.9,18.9,20.2]
x=np.array(months)
y=np.array(temprature)
plt.bar(x,y)
plt.xlabel("monthes of year")
plt.ylabel("temprature in degree celsius")
plt.show()


#7 bargraph to represent first six square numbers each with each different color bar
x=np.array(range(1,7))
y=np.array(np.square(x))
cl=np.array(['b','y','r','g','pink','orange'])
plt.bar(x,y,color=cl)
plt.xlabel("numbers")
plt.ylabel("square of numbers")
plt.show()

#8 bar graph to compare friends heights
friends_name=np.array(["Ram","Sham","Gopi","Samrat","Varun"])
heights=np.array([150,147,172,163,156])
plt.bar(friends_name,heights,color="g")
plt.show()
