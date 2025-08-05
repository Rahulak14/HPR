# 📊 Patients Dashboard Project using Pandas and Matplotlib

## Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

## Step 2: Sample Data Creation
import io

csv_text = """PatientID,Name,Age,Gender,VisitDate,Diagnosis,Treatment,Medication,LabResult_Hb,LabResult_BP_Sys,LabResult_BP_Dia,Outcome
P001,Asha R,45,F,2025-07-12,Hypertension,Lifestyle & Medication,Amlodipine,13.5,150,95,Stable
P002,Ravi K,60,M,2025-07-10,Diabetes Type 2,Diet & Insulin,Metformin,12.1,130,85,Improved
P003,Sneha M,30,F,2025-07-15,Anemia,Iron Supplementation,Ferrous Sulfate,9.2,120,80,Stable
P004,Manoj T,55,M,2025-07-18,Heart Disease,Surgery & Follow-up,Aspirin,14.0,140,90,Critical
P005,Lata V,70,F,2025-07-20,Hypertension & Diabetes,Dual Management,Losartan,11.5,160,100,Worsened
P006,Karan S,40,M,2025-07-11,Back Pain,Physiotherapy,exercise,None,125,82,Improved
P007,Nisha B,35,F,2025-07-17,PCOS,Diet & Hormonal Therapy,Metformin,12.6,118,78,Stable
P008,Vikram J,29,M,2025-07-16,Asthma,Inhalers & Lifestyle,Salbutamol,13.3,122,80,Improved
P009,Anjali D,50,F,2025-07-13,Thyroid Disorder,Medication,Levothyroxine,10.4,135,88,Stable
P010,Suresh N,65,M,2025-07-19,Chronic Kidney Disease,Dialysis,surgery,None,145,92,Critical
"""


#df = pd.DataFrame(data)
df = pd.read_csv(io.StringIO(csv_text))


#Line Plot - LabResult_BP_Sys Over Time
df.plot(x='PatientID', y='LabResult_BP_Sys', kind='line', marker='o', title='Patients Outcome')
plt.ylabel('LabResult_BP_Sys')
plt.grid(True)
plt.show()


#Line Plot - LabResult_BP_Dia Over Time
df.plot(x='PatientID', y='LabResult_BP_Dia', kind='line', marker='s', color='green', title='Monthly Profit')
plt.ylabel('LabResult_BP_Dia')
plt.grid(True)
plt.show()

#Line Plot - LabResult_Hb Over Time
df.plot(x='PatientID', y='LabResult_Hb', kind='line', marker='o', title='Patients Outcome')
plt.ylabel('LabResult_Hb')
plt.grid(True)
plt.show()

#Bar Plot - Age by PatientID
df.groupby('PatientID')['Age'].sum().plot(kind='bar', color='skyblue', title='Age by PatientID')
plt.ylabel('Age')
plt.xticks(rotation=0)
plt.show()

#Pie Chart - Age by PatientID
df.groupby('PatientID')['Age'].sum().plot(kind='pie', autopct='%1.1f%%', title='Age by PatientID')
plt.ylabel('')
plt.show()

#Save Plot
df.plot(x='PatientID', y='LabResult_Hb', kind='line')
plt.title('Patients Outcome')
plt.savefig('Patients_Outcome_plot.png', dpi=300, bbox_inches='tight')
plt.show()
