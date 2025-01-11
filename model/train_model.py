'''
@author RIT GDSC
@brief Train a machine learning model to predict optimal watering cycles and yield metrics based on historical data.
Tools: Scikit-learn for traditional ML models, Pandas for data manipulation, and joblib for lightweight pipelining in
Python.
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Sample soil data
soil_data = {
    'pH': [6.5, 7.0, 5.8, 6.2, 6.8],
    'Moisture': [20, 30, 25, 22, 28],
    'Nutrients': [50, 60, 55, 52, 58]
}

# Sample yield metrics (target variable)
yield_metrics = [100, 150, 120, 110, 140]

# Create a DataFrame
df = pd.DataFrame(soil_data)

# Features and target
X = df[['pH', 'Moisture', 'Nutrients']]
y = yield_metrics

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'model/random_forest_model.pkl')

# Optionally, you can evaluate the model's performance

predictions = model.predict(X_test)
print(f'Model predictions: {predictions}')
print(f'Actual values: {y_test}')