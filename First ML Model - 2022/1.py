
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

# how linear regration works

# calculate best fit line y=mx+b, it is predicted value

# m is slope and b is y intercept point

# sum of squared error = (mx1+b - actual_values)sqr +(mx2+b - actual_values_2)sqr +....+ (mxn+b - actual_values_n)sqr


diabetes = datasets.load_diabetes()

# print(diabetes.keys())
# ['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module']

# print(diabetes.DESCR)

diabetes_X = diabetes.data[:, np.newaxis, 2]

# diabetes_X = diabetes.data

diabetes_X_train = diabetes_X[:-30]

diabetes_X_test = diabetes_X[-30:]

diabetes_y_train = diabetes.target[:-30]

diabetes_y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()
model.fit(diabetes_X_train, diabetes_y_train)

predicted_x = model.predict(diabetes_X_test)

print("mean squared error is : ", mean_squared_error(
    diabetes_y_test, predicted_x))

print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)


plt.scatter(diabetes_X_test,diabetes_y_test)
plt.plot(diabetes_X_test,predicted_x)
plt.show()
