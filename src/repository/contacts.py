from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel, ContactUpdateModel


async def get_contacts(db: Session):
    contacts = db.query(Contact).all()
    return contacts


async def get_contact_by_id(contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact


async def get_contact_by_email(contact_email: str, db: Session):
    contact = db.query(Contact).filter_by(email=contact_email).first()
    return contact


async def get_contact_by_phone(contact_phone: str, db: Session):
    contact = db.query(Contact).filter_by(email=contact_phone).first()
    return contact


async def create_contact(body: ContactModel, db: Session):
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(body: ContactUpdateModel, contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    if contact:
        contact.phone = body.phone
        contact.email = body.email
        db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

