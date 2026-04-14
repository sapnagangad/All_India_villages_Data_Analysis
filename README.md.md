# 🇮🇳 All India Villages Data Pipeline & API

## Project Overview

This project is a complete backend data pipeline for handling All India village-level data.

It includes:

* Data cleaning using Python
* Data storage using MySQL
* REST API built using Node.js (Express)

---

## Technologies Used

* Python (Pandas)
* MySQL (Workbench)
* Node.js (Express.js)

---

## Project Structure

```
VILLAGE_PROJECT/
│
├── backend/                # Node.js API
│   ├── server.js
│   ├── package.json
│   └── package-lock.json
│
├── dataset/                # Raw dataset files
├── cleaned_villages.csv    # Cleaned dataset
├── data_cleaning.py        # Python script for cleaning
├── database.sql            # MySQL schema
└── .gitignore
```

---

## Data Cleaning (Python)

* Reads multiple raw dataset files
* Cleans and merges data
* Removes unnecessary rows
* Outputs a final cleaned CSV file

Run:

```
python data_cleaning.py
```

---

## Database Setup (MySQL)

### Step 1: Open MySQL Workbench

### Step 2: Create Database

```sql
CREATE DATABASE village_db;
```

### Step 3: Create Table

```sql
USE village_db;

CREATE TABLE villages (
    state_code INT,
    state_name VARCHAR(100),
    district_code INT,
    district_name VARCHAR(100),
    sub_district_code INT,
    sub_district_name VARCHAR(100),
    village_code INT,
    village_name VARCHAR(100)
);
```

### Step 4: Import Data

* Import `cleaned_villages.csv` into `villages` table using Workbench

---

## Run Backend API

### Step 1:

```
cd backend
npm install
```

### Step 2:

```
node server.js
```

### Step 3:

Open in browser:

```
http://localhost:3000/villages
```

---

## API Endpoints

| Endpoint            | Description            |
| ------------------- | ---------------------- |
| `/`                 | Check API status       |
| `/villages`         | Get village data       |
| `/states`           | Get all states         |
| `/districts/:state` | Get districts by state |
| `/search/:name`     | Search villages        |

---

## Features

* Clean and structured dataset
* Fast API responses
* Real-world dataset handling
* End-to-end data pipeline

---

## Author

Akshay Kumar
