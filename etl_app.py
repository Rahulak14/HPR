import pandas as pd 
from pymongo import MongoClient
import os
#ETL / ELT Pipeline for Employee Data
#Extract - csv to pandas DataFrame
hpr_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'patientrecord.csv'))

#Load - lake pandas DataFrame to MongoDB
client = MongoClient('mongodb+srv://akrahul14:geethaperumal@cluster0.twi6ykn.mongodb.net/')
db = client['lake_hpr']
collection = db['hprs']
collection.delete_many({})
collection.insert_many(hpr_df.to_dict('records'))
print('patient loaded to lake database')

#Transform - MongoDB to pandas DataFrame
hpr_df['LabResult_Hb'] = hpr_df['LabResult_Hb'].fillna(0)
Diagnosis_LabResult_Hb_df = hpr_df.groupby('Diagnosis')['LabResult_Hb'].sum().reset_index()


#Load - warehouse pandas DataFrame to MongoDB
db = client['warehouse_hpr']
collection = db['hprs']
collection.delete_many({})
collection.insert_many(hpr_df.to_dict('records'))
print('Processed patient loaded to warehouse database')
collection = db['Diagnosis_LabResult_df']
collection.delete_many({})
collection.insert_many(Diagnosis_LabResult_Hb_df.to_dict('records'))
print('Processed Diagnosis LabResult loaded to warehouse database')