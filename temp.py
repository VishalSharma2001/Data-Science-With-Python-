import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
data=pd.read_csv("data.csv")
data.head()
data.replace('?', np.nan, inplace=True)
cols=data.columns
for col in cols:
    median=data[col].median()
    data[col].fillna(median,inplace=True)
    real_x=data.iloc[:,:-1].values
    real_y=data.iloc[:,-1].values
    train_x,test_x,train_y,test_y=train_test_split(real_x,real_y,test_size=.2,random_state=0)
    sc=StandardScaler()
train_x=sc.fit_transform(train_x)
test_x=sc.fit_transform(test_x)
cls=KNeighborsClassifier(n_neighbors=5)
cls.fit(train_x,train_y)
pred_y=cls.predict(test_x)
print(pred_y)
print(test_y)
from matplotlib.colors import ListedColormap
x_set,y_set=test_x,test_y
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min()-1,stop=x_set[:,0].max()+1,step=0.01),
                  np.arange(start=x_set[:,1].min()-1,stop=x_set[:,1].max()+1,step=0.01))
plt.contourf(x1,x2,cls.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
            alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
            c=ListedColormap(('red','green'))(i),label=j)
plt.title('KNN test set')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()