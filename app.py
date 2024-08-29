import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data from a CSV file
df = pd.read_csv('Admission_Prediction.csv')

# Drop the Serial_No column if it exists
df = df.drop(columns=['Serial_No'], errors='ignore')

# Handle missing values (e.g., fill with mean)
df.fillna(df.mean(), inplace=True)

# Features and labels
X = df.drop(columns=['Chance_of_Admit'])
y = df['Chance_of_Admit']

# Standard Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Function for user input and prediction
def get_user_input():
    GRE_Score = float(input("Enter GRE Score: "))
    TOEFL_Score = float(input("Enter TOEFL Score: "))
    University_Rating = float(input("Enter University Rating: "))
    SOP = float(input("Enter SOP (Statement of Purpose) strength: "))
    LOR = float(input("Enter LOR (Letter of Recommendation) strength: "))
    CGPA = float(input("Enter CGPA: "))
    Research = int(input("Enter Research experience (1 for Yes, 0 for No): "))
    
    user_data = np.array([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]])
    user_data_scaled = scaler.transform(user_data)
    
    prediction = model.predict(user_data_scaled)
    return prediction

# Make a prediction based on user input
if __name__ == "__main__":
    prediction = get_user_input()
    print(f"The predicted chance of admission is: {prediction[0]:.2f}")
    if prediction >= 0.5:
        print("The candidate is likely to get admission.")
    else:
        print("The candidate is less likely to get admission.")
