import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import streamlit as st

# 1. Business Understanding
st.header("Business Understanding")
st.write("The goal is to understand the relationship between an independent variable X and a dependent variable y. We will use simple linear regression to model this relationship.")

# 2. Data Understanding
st.header("Data Understanding")
st.write("We will generate synthetic data to simulate a real-world scenario. You can specify the parameters of the data generation process below.")

# User-defined parameters
a = st.slider("Select the slope (a)", 0.0, 10.0, 2.0, 0.1)
b = st.slider("Select the intercept (b)", 0.0, 10.0, 5.0, 0.1)
noise = st.slider("Select the noise level", 0.0, 20.0, 10.0, 0.5)
num_points = st.slider("Select the number of data points", 10, 100, 50, 5)

# 3. Data Preparation
st.header("Data Preparation")
st.write("We generate random data for X and then generate y with the specified slope, intercept, and noise.")
# Generate random data for X
X = np.random.rand(num_points, 1) * 100
# Generate y with noise
y = a * X.flatten() + b + np.random.randn(num_points) * noise

# 4. Modeling
st.header("Modeling")
st.write("We use scikit-learn's LinearRegression to fit a model to the data.")
# Create a linear regression model
model = LinearRegression()
# Train the model
model.fit(X, y)

# 5. Evaluation
st.header("Evaluation")
st.write("We evaluate the model by visualizing the data and the fitted line. We also show the original and fitted parameters.")
# Get the model's predictions
y_pred = model.predict(X)
# Get the model's parameters
a_fit = model.coef_[0]
b_fit = model.intercept_

st.write(f"Original parameters: a={a}, b={b}")
st.write(f"Fitted parameters: a_fit={a_fit:.2f}, b_fit={b_fit:.2f}")

# Plot the results
fig, ax = plt.subplots()
ax.scatter(X, y, label="Data")
ax.plot(X, y_pred, color='red', label="Fitted line")
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

# 6. Deployment
st.header("Deployment")
st.write("This Streamlit application is the deployment of the linear regression model. You can interact with the parameters on the left to see how the model changes.")
