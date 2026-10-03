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

df = pd.read_csv("patients.csv")

print("======= ORIGINAL DATA ========")
print(df)

# Check missing values
print()
print("========= MISSING VALUES =========")
print(df.isnull().sum())

# Find missing wait times
print()
print("======== MISSING WAIT TIMES =========")
print(df[df["Wait_Time"].isnull()])

# Calculate average wait
average_wait = df["Wait_Time"].mean()

print()
print("Average wait:", average_wait)

# Check the Department has missing values
print()
print("========== MISSING VALUES IN DEPARTMENT =========")
print(df["Department"].isnull().sum())

# Fill missing wait times
df["Wait_Time"] = df["Wait_Time"].fillna(average_wait)

# Check after cleaning
print()
print("======== AFTER CLEANING ============")
print(df)

print()
print("Missing wait times:", df["Wait_Time"].isnull().sum())

# Replace missing values with Unknown in Department
print()
print("========= AFTER CLEANING IN DEPARTMENT =======")
df["Department"] = df["Department"].fillna("Unknown")
print(df["Department"])

# Save cleaned dataset
df.to_csv("patients_cleaned.csv", index=False)

print()
print("Cleaned dataset saved as patients_cleaned.csv")