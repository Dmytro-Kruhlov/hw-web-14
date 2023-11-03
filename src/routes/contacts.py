from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactModel, ResponseContact, ContactUpdateModel
from src.repository import contacts as repository_contacts

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=List[ResponseContact])
async def get_contacts(
    db: Session = Depends(get_db),
    firstname: str = Query(default=None),
    lastname: str = Query(default=None),
    email: str = Query(default=None),
):
    if firstname or lastname or email:
        contacts = await repository_contacts.get_contact_by_filter(
            db, firstname, lastname, email
        )
    else:
        contacts = await repository_contacts.get_contacts(db)

    if not contacts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No contacts found"
        )

    return contacts


@router.get("/{days}", response_model=List[ResponseContact])
async def get_contacts(days: int, db: Session = Depends(get_db)):
    contacts = await repository_contacts.contacts_per_days(days, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contacts


@router.get("/{contact_id}", response_model=ResponseContact)
async def get_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_id(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@router.post("/", response_model=ResponseContact, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_email(body.email, db)
    if contact:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Contact with email:{body.email} already exist!",
        )
    contact = await repository_contacts.create_contact(body, db)
    return contact


@router.patch("/{contact_id}", response_model=ResponseContact)
async def update_contact(
    body: ContactUpdateModel,
    contact_id: int = Path(ge=1),
    db: Session = Depends(get_db),
):
    owner = await repository_contacts.update_contact(body, contact_id, db)
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return owner


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.remove_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact
