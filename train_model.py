import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
# Load Dataset
df = pd.read_csv("student_data.csv")
print("Dataset Loaded Successfully!\n")
# Convert Absences to Attendance (%)
# Formula:
# Attendance = 100 - (Absences × 2)
# Limit the values between 0 and 100
df["Attendance"] = 100 - (df["absences"] * 2)
df["Attendance"] = df["Attendance"].clip(lower=0, upper=100)
# Rename columns (for readability)
df.rename(columns={
    "studytime": "StudyHours",
    "G1": "FirstSessionalMarks",
    "G2": "SecondSessionalMarks",
    "G3": "FinalMarks"
}, inplace=True)
# Select Features
X = df[[
    "StudyHours",
    "Attendance",
    "FirstSessionalMarks",
    "SecondSessionalMarks"
]]
# Target Variable
y = df["FinalMarks"]*5
# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
# Create Model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)
# Train Model
model.fit(X_train, y_train)
# Predict
predictions = model.predict(X_test)
# Evaluate Model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print("=" * 45)
print("AI MODEL TRAINED SUCCESSFULLY")
print("=" * 45)
print(f"Mean Absolute Error : {mae:.2f}")
print(f"R² Score            : {r2:.2f}")
# Save Model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/student_model.pkl")
print("\nModel saved successfully!")