from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import session
from app import crud, models,schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="kpa data",
    description="kpa data",
    version="1.0.0",
    )

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello kpa"}

@app.post("/form_data", response_model=schemas.FormDataResponse)
def create_form(form: schemas.FormDataCreate, db: session = Depends(get_db)):
    return crud.create_form_data(db, form)

@app.get("/form_data/{id}", response_model=schemas.FormDataResponse)
def get_form(id: int, db:session = Depends(get_db)):
    db_form_data = crud.get_form_data_by_id(db, id)
    if db_form_data is None:
        raise HTTPException(status_code=404, detail="Form data not found")
    return db_form_data
    