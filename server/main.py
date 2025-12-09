from fastapi import FastAPI
from sqlmodel import create_engine, Session
from models import User
from schemas import UserCreateBody, UserPublicBody, UserPublic

app = FastAPI()


@app.post("/api/users", response_model=UserPublicBody)
def create_user(data: UserCreateBody):
    """Create user."""
    engine = create_engine("sqlite:///db.sqlite")
    session = Session(engine)
    user = User(
        bio="",
        email=data.user.email,
        username=data.user.username,
        password=data.user.password,
    ).save(session)
    return UserPublicBody(
        user=UserPublic(
            email=user.email,
            bio=user.bio,
            username=user.username,
            image=user.image,
        )
    )
