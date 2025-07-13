Project Title: KPA API Assignment (FastAPI + PostgreSQL)

 

Tech Stack Used:

- Python 3.11 
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn
- Pydantic
- python-dotenv

 

Setup Instructions:

1. Clone this repository or download the zip.
2. Create a virtual environment:

   For Windows:
   python -m venv venv
   venv\Scripts\activate

3. Install required packages:

   pip install -r requirements.txt

4. Create PostgreSQL database manually:

   CREATE DATABASE kpa_db;

5. Create .env file in project root with this line:

   DB_URL=postgresql://postgres:admin123@localhost:5432/kpa_db 

6. Run the API server:

   py -m uvicorn app.main:app --reload 

 



Other Notes:

- ORM is handled using SQLAlchemy.
- Data validation is done using Pydantic.
- Environment variables are managed using python-dotenv.
- Code is modular and divided into routers, schemas, and models for clean separation.
 

"# KPA-API-ASSIGMENT" 
