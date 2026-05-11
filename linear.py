import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv("C:\\Users\\BLESSY\\Documents\\LinearRegression\\Salary_Data.csv")
print(df.head())
df.loc[2,"Salary"]=None
print(df)
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print(df)
X=df[["YearsExperience"]]
Y=df["Salary"]
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
prediction=model.predict(x_test)
print(x_test)
print("Predicted Salary:",prediction)




import matplotlib.pyplot as plt 
plt.scatter(X,Y)
plt.plot(X,model.predict(X))
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()