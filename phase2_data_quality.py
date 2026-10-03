import csv

with open("patients.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Patient_ID", "Department", "Wait_Time", "Outcome"])
    writer.writerow([101, "Emergency", 45, "Treated"])
    writer.writerow([102, "Cardiology", 20, "Discharged"])
    writer.writerow([103, "Radiology", 60, "Treated"])
    writer.writerow([104, "Surgery", 15, "Discharged"])
    writer.writerow([105, "Emergency", 90, "Admitted"])

print("CSV file created!")

import pandas as pd

# Load the patient data
df = pd.read_csv("patients.csv")

print("===== DATASET PREVIEW ======")
print(df.head())

print()
print("======== COLUMN NAMES =======")
print(df.columns.tolist())

print()
print("======== DATASET SIZE =======")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print()
print("====== DATA TYPES =====")
print(df.dtypes)

print()
print("======= MISSING VALUES ======")
print(df.isnull().sum())

print()
print("======= DATA QUALITY SUMMARY =======")

print("Duplicate rows:", df.duplicated().sum())
print("Missing Values:", df.isnull().sum().sum())

print()
print("========= DISPLAY THE MINIMUM, MAXIMUM AND AVERAGE WAIT TIME ==========")
print("Minimum wait:", df["Wait_Time"].min())
print("Maximum wait:", df["Wait_Time"].max())
print("Average wait:", df["Wait_Time"].mean())

print()
print("========== DISPLAY HOW MANY UNIQUE DEPARTMENTS ==========")
print("Number of departments:", df["Department"].nunique())