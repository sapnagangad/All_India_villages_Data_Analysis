import pandas as pd
import os
import mysql.connector

# STEP 1: Read all Excel files
folder_path = "dataset"
all_data = []

for file in os.listdir(folder_path):
    if file.endswith(".xls"):
        file_path = os.path.join(folder_path, file)
        print("Reading:", file)

        df = pd.read_excel(file_path)
        all_data.append(df)

# Merge all files
final_df = pd.concat(all_data, ignore_index=True)

print(final_df.head())
print("Total rows:", final_df.shape)

# STEP 2: Data Cleaning
# Remove unwanted columns
final_df = final_df.loc[:, ~final_df.columns.str.contains('^Unnamed')]

print("After removing unwanted columns:")
print(final_df.columns)

# Check missing values
print("Missing values:")
print(final_df.isnull().sum())

# Remove duplicates
final_df = final_df.drop_duplicates()

print("After removing duplicates:")
print(final_df.shape)

# Save cleaned data
final_df.to_csv("cleaned_villages.csv", index=False)
print("Cleaned file saved!")

# STEP 3: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",   # for your sql password
    database="village_db"
)

cursor = conn.cursor()
print("Connected to MySQL!")


# STEP 4: Create Table


cursor.execute("""
CREATE TABLE IF NOT EXISTS villages (
    state_code FLOAT,
    state_name VARCHAR(100),
    district_code FLOAT,
    district_name VARCHAR(100),
    sub_district_code FLOAT,
    sub_district_name VARCHAR(100),
    village_code FLOAT,
    village_name VARCHAR(150)
);
""")

conn.commit()
print("Table created!")

# STEP 5: Fast Data Insert

data = []

for index, row in final_df.iterrows():
    data.append((
        row['MDDS STC'],
        row['STATE NAME'],
        row['MDDS DTC'],
        row['DISTRICT NAME'],
        row['MDDS Sub_DT'],
        row['SUB-DISTRICT NAME'],
        row['MDDS PLCN'],
        row['Area Name']
    ))

cursor.executemany("""
INSERT INTO villages VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""", data)

conn.commit()

print("Data inserted successfully!")

# CLOSE CONNECTION

cursor.close()
conn.close()

print("All done")