from pydantic import BaseModel, EmailStr, Field
from datetime import date


class ContactModel(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    phone: str
    birthday: date


class ResponseContact(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: EmailStr
    phone: str
    birthday: date

    class Config:
        from_attributes = True


class ContactUpdateModel(BaseModel):
    email: EmailStr
    phone: str


