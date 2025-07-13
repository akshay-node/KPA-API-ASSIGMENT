from sqlalchemy.orm import Session
from . import models, schemas

def create_form_data(db: Session, form_data: schemas.FormDataCreate):
    db_entry = models.FormData(**form_data.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_form_data_by_id(db: Session, data_id: int):
    return db.query(models.FormData).filter(models.FormData.id == data_id).first()

