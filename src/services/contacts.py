from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.contacts import ContactRepository
from src.schemas import ContactCreate, ContactUpdate

class ContactService:
    def __init__(self, db: AsyncSession):
        self.repository = ContactRepository(db)

    async def create_contact(self, body: ContactCreate):
        return await self.repository.create_contact(body)

    async def get_contacts(self, skip: int, limit: int, query: Optional[str]=None):
        return await self.repository.get_contacts(skip, limit, query)

    async def get_birthdays(self):
        return await self.repository.get_birthdays()

    async def get_contact(self, contact_id: int):
        return await self.repository.get_contact_by_id(contact_id)

    async def update_contact(self, contact_id: int, body: ContactUpdate):
        return await self.repository.update_contact(contact_id, body)

    async def remove_contact(self, contact_id: int):
        return await self.repository.remove_contact(contact_id)