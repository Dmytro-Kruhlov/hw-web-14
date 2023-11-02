from pydantic import BaseModel, EmailStr, Field


class ContactModel(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    phone: str
    birthday: str


class ResponseContact(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: EmailStr
    phone: str
    birthday: str

    class Config:
        from_attributes = True


class ContactUpdateModel(BaseModel):
    email: EmailStr
    phone: str


