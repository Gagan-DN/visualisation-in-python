import numpy as np
import matplotlib.pyplot as plt

#FOR PIE CHART
#17 pie chart to represent share of five different brands
mylables=np.array(["HP","DELL","LENOVA","ASUS","OTHERS"])
share=np.array([162,89,38,64,7])
plt.pie(share,labels=mylables,startangle=90,shadow=True)
plt.legend()
plt.show()

#18 pie chart to show percentage of time spent
# on different activities in a typical day
mylables=np.array(["sleeping","eating","working","gym","others"])
time_spent=np.array([37.5,8.4,41.7,16.6,20.8])
plt.pie(share,labels=mylables,startangle=90,shadow=True)
plt.legend()
plt.show()

#19 pie chart to represent budget is categories
#like rent,food,entertainment,savings,emi,miscellaneous
mylables=np.array(["rent","food","entertainment","savings","emi","miscellaneous"])
account=np.array([18000,4670,2000,6500,3000,1500])
myexp=[0,0,0,0.1,0,0]
plt.pie(account,labels=mylables,startangle=90,shadow=True,explode=myexp)
plt.legend()
plt.show()

#20 pie chart to illustrate composition of gases in earth atmosopher
mylables=np.array(["Hydrogen","Oxygen","Carbon-dioxide","Nitrogen","Others"])
shared=np.array([64,32,3,87,7])
myexp=[0,0.1,0,0,0]
plt.pie(shared,labels=mylables,startangle=90,shadow=True,explode=myexp)
plt.legend()
plt.show()
