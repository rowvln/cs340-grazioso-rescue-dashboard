# CS 340 – Grazioso Salvare Rescue Dashboard

## Repository Contents

This repository contains the complete implementation of the Grazioso Salvare Rescue Candidate Dashboard:

- `ProjectTwoDashboard.ipynb` – JupyterDash application that renders the interactive dashboard  
- `CRUD_Python_Module.py` – Custom MongoDB CRUD module used to connect the dashboard to the database  
- `Grazioso Salvare Logo.png` – Branding image used in the dashboard interface  
- `rdizon_CS340_README_Module7.docx` – Formal Word README submitted for Project Two  

---

## Portfolio Reflection

### How I Write Maintainable, Readable, and Adaptable Programs

Maintainability starts with structure. In this project, I separated database logic from the user interface by creating a dedicated `AnimalShelterCRUD` class inside `CRUD_Python_Module.py`. This module establishes the MongoDB connection using parameterized credentials and encapsulates all database interactions inside reusable methods.

Instead of embedding database queries directly inside the dashboard notebook, I imported the CRUD module into `ProjectTwoDashboard.ipynb`. This allowed the dashboard to focus purely on interaction and visualization while the module handled data retrieval.

Advantages of this approach:

- Clear separation of concerns  
- Improved readability  
- Easier debugging  
- Reusability across projects  
- Reduced code duplication  

If the database schema changes, I only need to modify the CRUD module rather than rewriting dashboard logic.

In the future, this module could support:

- A REST API  
- A reporting dashboard  
- A larger rescue management system  
- A production web application outside of JupyterDash  

This reflects real-world backend architecture practices rather than assignment-only coding.

---

### How I Approach Problems as a Computer Scientist

For this project, I approached the requirements as a systems design problem rather than just a coding task.

Grazioso Salvare needed to identify rescue-training candidates using specific criteria. That required:

1. Designing efficient MongoDB queries  
2. Structuring filter logic correctly  
3. Keeping dashboard components synchronized  
4. Handling edge cases such as missing or malformed coordinates  

In earlier programming assignments, I often focused on making the output work. In this project, I shifted toward thinking about:

- Performance  
- Scalability  
- Client/server architecture  
- Defensive programming  

Instead of filtering data purely in Pandas, I pushed filtering logic into MongoDB queries. That mirrors how production systems handle large datasets.

In future database projects, I would:

- Define data and filtering requirements before implementation  
- Design indexes strategically for performance  
- Separate data access logic from user interface logic  
- Anticipate invalid input and edge cases  

This project strengthened my ability to think like a software engineer designing a system rather than just completing a feature.

---

### What Computer Scientists Do and Why It Matters

Computer scientists build systems that transform raw data into actionable insight.

In this project, thousands of animal records were turned into:

- An interactive data table  
- A dynamic breed distribution pie chart  
- A geolocation map  
- Rescue-type filtering controls  

Instead of manually reviewing spreadsheets, Grazioso Salvare can quickly identify potential rescue candidates based on defined criteria.

This improves:

- Decision-making speed  
- Operational efficiency  
- Data accuracy  
- Resource allocation  

This dashboard is not just code. It is a tool that helps an organization operate more intelligently.

For me personally, this project reflects my transition into engineering-focused thinking. It combines backend logic, database design, and user-centered interaction. That intersection of data systems and product functionality is where I want to continue building my career.

---

## Technologies Used

- Python  
- MongoDB  
- PyMongo  
- JupyterDash  
- Dash DataTable  
- Dash Leaflet  
- Pandas  
- Plotly  

---

## How to Run the Dashboard

### Ensure MongoDB Is Running

Make sure MongoDB is installed and running locally.

The `aac` database must contain the `animals` collection with the modified Austin Animal Center dataset.

### Install Dependencies

```bash
pip install pymongo dash dash-leaflet pandas plotly
```
---
## Launch the Application

1. Open `ProjectTwoDashboard.ipynb`  
2. Run all cells in order  
3. The dashboard will launch in your browser  

---

## Author

Rowvin Dizon  
CS 340 – Client/Server Development  

Southern New Hampshire University

