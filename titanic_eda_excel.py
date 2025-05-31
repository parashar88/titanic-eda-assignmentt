# titanic_eda_excel.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from Excel
df = pd.read_excel("dataset3.xlsx")
print("✅ Dataset loaded!")

# See basic info
print("\nData info:\n", df.info())
print("\nMissing values:\n", df.isnull().sum())

# Clean missing Age and Embarked values
df['Age'].fillna(df['Age'].median(), inplace=True)
if 'Embarked' in df.columns:
    df.dropna(subset=['Embarked'], inplace=True)

print("\n✅ Cleaned missing values.\n")

# Grouping: survival by gender
print("\n📊 Survival by Gender:")
print(df.groupby('Sex')['Survived'].mean())

# Grouping: survival by class
print("\n📊 Survival by Class:")
print(df.groupby('Pclass')['Survived'].mean())

# Plot: Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.savefig('age_distribution.png')
plt.close()

# Plot: Survival by class and gender
plt.figure(figsize=(8, 5))
sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df)
plt.title('Survival by Class & Gender')
plt.savefig('survival_by_class_gender.png')
plt.close()

# Plot: Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.close()

print("\n✅ All graphs saved!")
