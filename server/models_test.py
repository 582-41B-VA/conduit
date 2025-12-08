from models import User
from sqlmodel import create_engine, Session, SQLModel


def get_session() -> Session:
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    return Session(engine)


def test_user_get():
    """Get user matching the id."""
    session = get_session()
    User(email="bob@mail.com", username="bob", password="secret", bio="").save(
        session
    )
    bob = User.get(session, 1)
    assert bob is not None
    assert bob.username == "bob"


