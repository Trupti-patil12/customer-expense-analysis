import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel("customer_expenses.xlsx")
print(df.info())
print(df.head())
#print(df.info)
print(df.columns)

#missing value handling
print("\nMissing values before cleaning:")
print(df.isnull().sum())

#drop column
df=df.dropna(subset=["Amount"])
#fill missing value
cols=['Customer_Name', 'Category','Payment_Mode', 'Location']
df[cols]=df[cols].fillna('unknown')

print("\nMissing values after cleaning:")
print(df.isnull().sum())

#outlier detection(IQR)
q1=np.percentile(df['Amount'],25)
q3=np.percentile(df['Amount'],75)
IQR=q3-q1
lower=q1-(1.5*IQR)
upper=q3+(1.5*IQR)
outliers=df[(df['Amount']<lower) | (df['Amount']>upper)]
print("Outliers rows:")
print(outliers)

#box plot(Outlier Visualization)
plt.boxplot(df['Amount'])
plt.title("Box Plot of Customer Expenses")
plt.ylabel('Amount')
plt.show()

#kpi calculation
total_spend=df['Amount'].sum()
avg_spend=df['Amount'].mean()
max_spend=df['Amount'].max()

print("\nKPI Metrics")
print("Total spend:",total_spend)
print("Average spend:",avg_spend)
print("maximum spend",max_spend)

#category wise calculation
category_spend=df.groupby('Category')['Amount'].sum()
category_spend = category_spend.sort_values(ascending=False)
print("category wise spending")
print(category_spend)

plt.figure()
category_spend.plot(kind='bar')
plt.title("total spending by category",fontsize=14)
plt.ylabel("Amount",fontsize=12)
plt.xlabel("Category",fontsize=12)
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()

#payment mode distribution
payment_count=df['Payment_Mode'].value_counts()

plt.figure()
payment_count.plot(kind="pie",autopct='%1.1f%%')
plt.title("payment mode distribution")
plt.ylabel("")
plt.show()

#location-wise spending
location_spend=df.groupby('Location')['Amount'].sum().sort_values(ascending=False)

plt.figure()
location_spend.plot(kind='bar')
plt.title("total spending by location",fontsize=14)
plt.ylabel('Amount',fontsize=12)
plt.xlabel('Location',fontsize=12)
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.show()

#Export Clean Data (For Power BI)
df.to_csv("clean_customer_expenses.csv", index=False)
print("\nClean data exported as clean_customer_expenses.csv")