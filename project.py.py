import pandas as pd

# Load dataset
df = pd.read_csv('student_dataset_v2.csv')

print("===== DATA =====")
print(df.head())

# Shape
print("\nShape:", df.shape)

# Columns
print("\nColumns:", df.columns)

# Data types
print("\nData Types:\n", df.dtypes)

# Missing values
print("\nMissing Values:\n", df.isnull().sum())

# Fill missing Marks
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# Analysis
print("\nHighest Attendance:", df['Attendance'].max())
print("Average Study Hours:", df['StudyHours'].mean())

# Top students
top = df.sort_values(by='Marks', ascending=False).head(5)
print("\nTop 5 Students:\n", top)
import pandas as pd
import matplotlib.pyplot as plt

# CSV file load karo
data = pd.read_csv("student_dataset_v2.csv")

# Data check karo
print(data.head())

# Example graph (assume columns: marks, study_hours)
plt.scatter(data['StudyHours'], data['Marks'])

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.grid(True)
plt.show()