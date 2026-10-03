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

#============================================
#   KPI CALCULATIONS
#============================================

total_patients = len(df)

average_wait = df["Wait_Time"].mean()

median_wait = df["Wait_Time"].median()

longest_wait = df["Wait_Time"].max()

shortest_wait = df["Wait_Time"].min()

long_waits = df[df["Wait_Time"] > 60]

long_wait_percentage = (len(long_waits) / len(df)) * 100

long_wait_count = len(long_waits)

department_counts = df["Department"].value_counts()

top_department = department_counts.index[0]

number_of_departments = df["Department"].nunique()

emergency_visits = len(df[df["Department"] == "Emergency"])

#==========================================================
#   DISPLAY KPIs
#=========================================================

print("=================================================================")
print(" HEALTHCARE KPI REPORT")
print("==================================================================")

print()

print("Total Patients:", total_patients)

print("Average Wait:", round(average_wait, 1), "minutes")

print("Median Wait:", round(median_wait, 1), "minutes")

print("Shortest:", shortest_wait, "minutes")

print("Longest Wait:",  longest_wait, "minutes")

print("Long-Wait Percentage:", round(long_wait_percentage, 1), "%")

print("Long-Wait Patients:", long_wait_count)

print("Top Department:", top_department)

print("Number of Departments:", number_of_departments)

print("Emergency Visits:", emergency_visits)

# Create a KPI Dictionary

kpis = {
    "Total Patients": total_patients, "Average Wait": round(average_wait, 1),
    "Median Wait": round(median_wait, 1), "Shortest Wait": shortest_wait, "Longest Wait": longest_wait,
    "Long-Wait Percentage": round(long_wait_percentage, 1), "Top Department": top_department, "Number of Departments": number_of_departments
    }
    
print()
print("============ KPI DICTIONARY ===========")
print(kpis)

# Save the KPI report
kpi_data = pd.DataFrame(list(kpis.items()), columns = ["KPI", "Value"])

kpi_data.to_csv("healthcare_kpis.csv", index=False)

print()
print("KPI report saved as healthcare_kpis.csv")