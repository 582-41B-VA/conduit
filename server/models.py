from sqlmodel import Field, SQLModel, Session
from typing import Self


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str
    username: str
    password: str
    bio: str
    image: str | None = Field(default=None)

    @classmethod
    def get(cls, session: Session, id: int) -> Self | None:
        """Return an instance matching the id or None if none was found."""
        return session.get(cls, id)

    def save(self, session: Session) -> Self:
        """Save instance to the DB and update fields (e.g., id)."""
        session.add(self)
        session.commit()
        session.refresh(self)
        return self
