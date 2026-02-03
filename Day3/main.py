import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample dataset
data = {
    "Age": [18, 22, 25, 30, 35, 40, 45, 50],
    "Salary": [15000, 22000, 30000, 45000, 60000, 75000, 90000, 110000],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR"]
}

df = pd.DataFrame(data)

# Histogram
sns.histplot(df["Age"], kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
sns.scatterplot(x="Age", y="Salary", data=df)
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# Bar Chart
sns.countplot(x="Department", data=df)
plt.title("Department Count")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()
