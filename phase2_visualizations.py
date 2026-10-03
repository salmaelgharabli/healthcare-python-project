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
import os

df = pd.read_csv("patients.csv")

# Clean column names
df.columns = df. columns.str.strip()

# Create charts folder
os.makedirs("charts", exist_ok=True)

print("Columns:", df.columns.tolist())


#=============================================================
#   CHART 1: PATIENTS BY DEPARTMENT
#=============================================================

department_counts = df["Department"].value_counts()

plt.figure(figsize=(8,5))

department_counts.plot(kind="bar")

plt.title("Patients by Department")
plt.xlabel("Department")
plt.ylabel("Number of Patients")

plt.tight_layout()

plt.savefig("charts/patients_by_department.png")

plt.show()
plt.close()



#==================================================================
#   CHART 2: AVERAGE WAIT BY DEPARTMENT
#==================================================================

average_wait = df.groupby("Department")["Wait_Time"].mean()

plt.figure(figsize=(8, 5))

average_wait.plot(kind="bar")

plt.title("Average Wait Time by Department")
plt.xlabel("Department")
plt.ylabel("Average Wait Time (minutes)")

plt.tight_layout()

plt.savefig("charts/average_wait_by_department.png")

plt.show()
plt.close()




#=======================================================================
#   CHART 3: WAIT-TIME DISTRIBUTION
#=======================================================================

plt.figure(figsize=(8, 5))

plt.hist(df["Wait_Time"], bins=5)

plt.title("Distribution of Patient Wait Times")

plt.xlabel("Wait Time (minutes)")
plt.ylabel("Number of Patients")

plt.tight_layout()

plt.savefig("charts/wait_time_distribution.png")

plt.show()
plt.close()




#============================================================================
#   CHART 4: TOP 5 LONGEST WAITS
#============================================================================

top_5 = df.sort_values("Wait_Time", ascending=False).head(5)

plt.figure(figsize=(8, 5))

plt.barh(top_5["Patient_ID"].astype(str), top_5["Wait_Time"])

plt.title("Top 5 Longest Patient Waits")
plt.xlabel("Wait Time (minutes)")
plt.ylabel("Patient ID")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig("charts/top_5_longest_waits.png")

plt.show()
plt.close()


#===================================================================
#   CHART 5: PATIENT OUTCOMES
#===================================================================

if "Outcome" in df.columns:
    outcome_counts = df["Outcome"].value_counts()
    plt.figure(figsize=(8, 5))
    
    outcome_counts.plot(kind="bar")
    
    plt.title("Patient Outcomes")
    plt.xlabel("Outcome")
    plt.ylabel("Number of Patients")
    
    plt.tight_layout()
    
    plt.savefig("charts/patient_outcomes.png")
    
    plt.show()
    plt.close()
else:
    print()
    print("Outcome column not found.")
    print("Skipping outcome chart.")

print()
print("All charts created successfully!")