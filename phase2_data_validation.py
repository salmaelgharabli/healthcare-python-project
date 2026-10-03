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

print("===== DATA =====")
print(df)

# Check negative waits
negative_waits = df[df["Wait_Time"] < 0]

print()
print("======== NEGATIVE WAIT TIMES ==========")
print(negative_waits)

# Check very long waits
long_waits = df[df["Wait_Time"] > 180]

print()
print("============= VERY LONG WAIT TIMES ============")
print(long_waits)

# Check departments
print()
print("========== DEPARTMENTS =========")
print(df["Department"].unique())

# Remove accidental spaces
df["Department"] = df["Department"].str.strip()

# Check duplicate Patient IDs
duplicate_ids = df[df["Patient_ID"].duplicated()]

print()
print("====== DUPLICATE PATIENT IDs =========")
print(duplicate_ids)

# Validate wait times
invalid_waits = df[(df["Wait_Time"] < 0) | (df["Wait_Time"] > 180)]

# Check for duplicate rows
print("Duplicate rows:", df.duplicated().sum())

print()
print("======= WAIT TIMES NEEDING REVIEW =======")
print(invalid_waits)

# Validation summary
print()
print("========== VALIDATION SUMMARY ==========")

print("Duplicate Patient IDs:", df["Patient_ID"].duplicated().sum())

print("Invalid Wait Time:", len(invalid_waits))

print("Number of Departments:", df["Department"].nunique())
