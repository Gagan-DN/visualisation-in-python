import numpy as np
import matplotlib.pyplot as plt
#FOR BARH (HORIZONTAL BAR CHARTS)

#9 horizontal bar chart showing numbers of books read in semister
num_students=np.array([6,4,5,7,13,8])
num_books_read=np.array([56,34,45,13,5,40])
plt.barh(num_students,num_students,color="b")
plt.xlabel("number of books")
plt.ylabel("number of students")
plt.show()

#10 use barh to show time(s) taken by different animals to run 100 meters
animals=np.array(["Cow","Dog","Cat","Tiger","Cheeta"])
time=np.array([300,180,160,132,102])
plt.barh(animals,time)
plt.xlabel("time(s)")
plt.ylabel("animals")
plt.show()


#11 use barh display points scored by a players on a basketball team
player=np.array(["a","b","c","d","e","f","g"])
points=np.array([3,6,5,12,6,9,10])
plt.barh(player,points,color='g')
plt.xlabel("players")
plt.ylabel("points scored")
plt.show()

#12 use barh to show popularity of different programing languages based on scale 1-10
lang=np.array(["html","css","python","java_script","java","c"])
rating=np.array([6.2,4.8,7.9,8.6,7.4,5.9])
plt.barh(lang,rating)
plt.xlabel('popularity')
plt.ylabel("programing languages")
plt.show()
