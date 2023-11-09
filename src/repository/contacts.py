
from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel, ContactUpdateModel
from datetime import date, timedelta


async def get_contacts(db: Session):
    contacts = db.query(Contact).all()
    return contacts


async def get_contact_by_id(contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).all()
    return contact


async def get_contact_by_email(contact_email: str, db: Session):
    contact = db.query(Contact).filter_by(email=contact_email).all()
    return contact


async def get_contact_by_filter(db: Session, firstname: str = None, lastname: str = None, email: str = None, ):
    query = db.query(Contact)

    if firstname:
        query = query.filter(Contact.firstname == firstname)
    if lastname:
        query = query.filter(Contact.lastname == lastname)
    if email:
        query = query.filter(Contact.email == email)

    contacts = query.all()
    return contacts


async def get_contact_by_lastname(db: Session, firstname: str=None, lastname: str=None, email: str=None, ):
    contact = db.query(Contact).filter_by(lastname=lastname).all()
    return contact


async def create_contact(body: ContactModel, db: Session):
    contact = Contact(**body.model_dump())
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


async def contacts_per_days(days: int, db: Session):
    today = date.today()
    future_date = today + timedelta(days)
    today_str = today.strftime("%Y-%m-%d")
    future_date_str = future_date.strftime("%Y-%m-%d")
    contacts = db.query(Contact).filter(Contact.birthday > today_str, Contact.birthday <= future_date_str).all()
    return contacts
