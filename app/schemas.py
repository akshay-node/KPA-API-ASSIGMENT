from pydantic import BaseModel , validator

class FormDataBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str


@validator('address')
def address_must_not_Empty(cls,value):
    if not value.strip():
        raise ValueError('Address must not be empty')
    return value


class FormDataCreate(FormDataBase):
    pass


class FormDataResponse(FormDataBase):
    id: int
    class Config:
        orm_mode = True
