# 📊 Customer Expense & Spending Analysis  
### Agneyra Internship – Second Project

## 📌 Project Overview
This project was developed as part of my **Data Analytics Internship at Agneyra**.  
The objective of this project is to analyze customer expense data, clean and validate it using Python, perform Exploratory Data Analysis (EDA), and finally build an interactive dashboard in Power BI to understand spending behavior and trends.

## 🎯 Project Objective
- Analyze customer spending behavior
- Identify category-wise and location-wise spending patterns
- Calculate key KPIs for decision-making
- Create a professional and interactive dashboard

## 🛠️ Tools & Technologies Used
- **Excel** (Raw Data Source)
- **Python**
  - Pandas
  - NumPy
  - Matplotlib
- **Power BI** (Dashboard & Visualization)
- 
## 📂 Dataset Information
- **Initial Format:** Excel (`customer_expenses.xlsx`)
- **Final Format:** CSV (`clean_customer_expenses.csv`)
- **Data Fields:**
  - Customer_Name
  - Category
  - Amount
  - Payment_Mode
  - Location
  - Date

## 🔁 Project Workflow (End-to-End Pipeline)

### Step 1: Data Collection (Excel)
- Collected customer expense data in Excel format.
- Verified basic structure and columns.
  
### Step 2: Data Cleaning using Python
- Loaded Excel data into Python using Pandas.
- Checked dataset structure using:
  - `df.info()`
  - `df.head()`
  - `df.columns`

#### Missing Value Handling:
- Identified missing values using `df.isnull().sum()`
- Dropped rows where **Amount** was missing.
- Filled missing values in:
  - Customer_Name
  - Category
  - Payment_Mode
  - Location  
  with **"unknown"**

### Step 3: Exploratory Data Analysis (EDA)
- Performed statistical analysis on expense data.
- Calculated quartiles (Q1, Q3) and IQR.
- Detected outliers using the **IQR method**.
- Visualized outliers using a **Box Plot**.

### Step 4: KPI Calculation
Calculated important business KPIs:
- **Total Spend**
- **Average Spend**
- **Maximum Spend**
- **Number of Transactions**

### Step 5: Data Visualization in Python
- **Category-wise spending** using Bar Chart
- **Payment mode distribution** using Pie Chart
- **Location-wise spending** using Bar Chart

### Step 6: Export Clean Data
- Exported cleaned and processed data into:
  - `clean_customer_expenses.csv`
- This CSV file was used as input for Power BI.

### Step 7: Power BI Dashboard Creation
- Imported cleaned CSV file into Power BI.
- Created interactive dashboard with:
  - KPI Cards
  - Category-wise spending analysis
  - Location-wise spending analysis
  - Payment mode distribution
  - Time-based spending trend
- Added slicers for dynamic filtering.
- Exported dashboard as **PDF** https://github.com/Trupti-patil12/customer-expense-analysis/blob/main/costomer_expenses_dashbord.pdf.

## 📈 Dashboard Features
- Interactive KPI cards
- Dynamic charts with slicers
- Clean and professional layout
- Business-focused insights

##  Key Insights
- Certain categories show significantly higher spending.
- A few locations contribute the majority of total expenses.
- Digital payment modes are more frequently used.
- Some customers show unusually high spending behavior (outliers).

## 📌 Key Learnings
- Data cleaning and preprocessing using Python
- Handling missing values and outliers
- Performing Exploratory Data Analysis (EDA)
- Data visualization using Matplotlib
- Dashboard creation using Power BI
- End-to-end data analytics workflow

## 🚀 Conclusion
This project demonstrates a complete **end-to-end data analytics pipeline**, starting from raw Excel data to a clean, insightful Power BI dashboard.  
It helped strengthen my understanding of data cleaning, analysis, and visualization techniques.

## 🏢 Internship Details
- **Company:** Agneyra  
- **Project Type:** Major Project  
- **Project Number:** Second Project  
- **Email:** agneyra63@gmail.com  
- **URN:** UDYAM-AP-01-011115

---


