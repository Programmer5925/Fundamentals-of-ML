import pandas as pd

df = pd.read_csv("titanic_large.csv")   

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing values in each column:")
print(df.isnull().sum())

df['Age'].fillna(df['Age'].mean(), inplace=True)

df.dropna(subset=['Embarked'], inplace=True)

filtered_df = df[df['Age'] > 30][['Name', 'Age', 'Sex', 'Survived']]
print("\nFiltered Data (Age > 30):")
print(filtered_df.head())

grouped_data = df.groupby('Sex')['Age'].mean()
print("\nAverage Age by Gender:")
print(grouped_data)

