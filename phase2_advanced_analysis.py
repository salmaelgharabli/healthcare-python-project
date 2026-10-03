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

# Clean column names 
df.columns = df.columns.str.strip()

print("=========== DATASET ==========")
print(df)

# Department counts
department_counts = df["Department"].value_counts()

print("======= VISITS BY DEPARTMENT =======")
print(department_counts)

# Average wait by department
average_wait = df.groupby("Department")["Wait_Time"].mean()

print()
print("========= AVERAGE WAIT BY DEPARTMENT ========")
print(average_wait)

# Highest average wait
highest_wait_department = average_wait.idxmax()
highest_average_wait = average_wait.max()

print()
print("Department with highest average wait:", highest_wait_department)

print("Average wait:", round(highest_average_wait, 1), "minutes")

# Long waits
long_waits = df[df["Wait_Time"] > 60]

print()
print("========= LONG-WAIT PATIENTS ==========")
print(long_waits)

# Long-wait percentage
long-wait_percentage = (len(long_waits) / len(df)) * 100

print()
print("Percentage of patients with long waits:", round(long_wait_percentage, 1), "%")

# Statistical Summary
print()
print("========== WAIT TIME STATISTICS ==========")
print(df["Wait_Time"].describe())

# KPI Summary
print()
print("======================================================")
print(" HEALTHCARE KPI SUMMARY")
print("======================================================")

print("Total patients:", len(df))

print("Average wait:", round(df["Wait_Time"].mean(), 1), "minutes")

print("Shortest wait:", df["Wait_Time"].min(), "minutes")

print("Top department:", department_counts.index[0])

print("Long-wait percentage:", round(long_wait_percentage, 1), "%")

# Calculate the median wait time
median_wait = df["Wait_Time"].median()
print("Median wait:", (median_wait), "minutes")

# Find three patients with the longest wait
print()
print("============== TOP 3 PATIENTS WITH THE LONGEST WAIT =================")

top_3 = df.sort_values("Wait_Time", ascending=False).head(3)

print(top_3[["Patient_ID", "Department", "Wait_Time"]])