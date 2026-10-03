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
import matplotlib.pyplot as plt

#===========================================================
#   LOAD DATA
#===========================================================

df = pd.read_csv("patients.csv")

# Clean column names
df.columns = df.columns.str.strip()

#============================================================
#   CALCULATE KPIs
#============================================================

total_patients = len(df)

average_wait = df["Wait_Time"].mean()

longest_wait = df["Wait_Time"].max()

shortest_wait = df["Wait_Time"].min()

department_counts = df["Department"].value_counts()

top_department = department_counts.index[0]

long_waits = df[df["Wait_Time"] > 60]

long_wait_percentage = (len(long_waits)/ len(df)) * 100

median_wait = df["Wait_Time"].median()

emergency_visits = len(df[df["Department"] == "Emergency"])


#==================================================================
#   DISPLAY DASHBOARD KPIs
#==================================================================

print("===========================================================")
print(" HEALTHCARE PATIENT DASHBOARD")
print("===========================================================")

print()

print("Total Patients:", total_patients)

print("Average Wait:", round(average_wait, 1), "minutes")

print("Longest Wait:", longest_wait, "minutes")

print("Shortest Wait:", shortest_wait, "minutes")

print("Top Department:", top_department)

print("Long-Wait Percentage:", round(long_wait_percentage, 1), "%")

print("Median Wait:", median_wait, "minutes")

print("Emergency Visits:", emergency_visits)


#=======================================================================
#   PATIENTS BY DEPARTMENT
#=======================================================================

plt.figure(figsize=(8, 5))

department_counts.plot(kind="bar")

plt.title("Patients by Department")
plt.xlabel("Department")
plt.ylabel("Number of Patients")

plt.tight_layout()

plt.savefig("patients_by_department_dashboard.png")

plt.show()
plt.close()


#============================================================================
#   AVERAGE WAIT BY DEPARTMENT
#============================================================================

average_by_department = (df.groupby("Department")["Wait_Time"].mean())

plt.figure(figsize=(8, 5))

average_by_department.plot(kind="bar")

plt.title("Average Wait Time by Department")
plt.xlabel("Department")
plt.ylabel("Average Wait Time (minutes)")

plt.tight_layout()

plt.savefig("average_wait_by_department_dashboard.png")

plt.show()
plt.close()



#================================================================================
#   TOP 5 LONGEST WAITS
#================================================================================

top_5 = df.sort_values("Wait_Time", ascending=False).head(5)

plt.figure(figsize=(8, 5))

plt.bar(top_5["Patient_ID"].astype(str), top_5["Wait_Time"])

plt.title("Top 5 Longest Patient Waits")
plt.xlabel("Patient ID")
plt.ylabel("Wait Time (minutes)")

plt.tight_layout()

plt.savefig("top_5_longest_waits_dashboard.png")

plt.show()
plt.close()

#==================================================================================
#   FINISHED
#==================================================================================

print()
print("========================================================================")
print("Dashboard analysis completed successfully!")
print("=========================================================================")