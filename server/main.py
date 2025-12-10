from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import create_engine, Session
from models import User
from schemas import UserCreateBody, UserPublicBody, UserPublic

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])


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


@app.get("/api/users", response_model=UserPublicBody)
def get_user():
    """Return currently authenticated user."""
    # TODO: Should get currently authenticated user.
    engine = create_engine("sqlite:///db.sqlite")
    session = Session(engine)
    user = User.get(session, 1)
    # TODO: Check requirements for 404
    if not user:
        return 404
    return UserPublicBody(
        user=UserPublic(
            email=user.email,
            bio=user.bio,
            username=user.username,
            image=user.image,
        )
    )
