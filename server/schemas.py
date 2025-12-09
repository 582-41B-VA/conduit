from sqlmodel import SQLModel


class UserPublic(SQLModel):
    email: str
    username: str
    bio: str
    image: str | None
    # TODO: token: ...


class UserCreate(SQLModel):
    username: str
    email: str
    password: str


class UserCreateBody(SQLModel):
    user: UserCreate


class UserPublicBody(SQLModel):
    user: UserPublic
