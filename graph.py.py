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