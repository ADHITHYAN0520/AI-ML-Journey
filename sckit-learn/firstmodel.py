from sklearn.linear_model import LinearRegression
#Train data
X = [[1],[2],[3],[4],[5],[6],[7]]
#Target values
y = [35,42,50,60,70,78,85]
#create the model
model = LinearRegression()
#Train model
model.fit(X,y)
#prediction
prediction = model.predict([[8]])
print("Predicted Score:", prediction[0])