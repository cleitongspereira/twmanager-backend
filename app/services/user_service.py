from typing import Optional
from sqlalchemy.orm import Session
from app.repositories.user_repository import get_by_email, create
from app.models.user import User
from app.core.security import hash_password, verify_password
from app.schemas.user import UserCreate

def create_user(db: Session, data: UserCreate) -> User:
    if get_by_email(db, data.email):
        raise ValueError("E-mail já cadastrado")

    user = User(
        name=data.name,
        email=data.email,
        nickname=data.nickname,
        password_hash=hash_password(data.password)
    )

    return create(db, user)

def authenticate_user(
    db: Session,
    email: str,
    password: str
) -> Optional[User]:
    user = get_by_email(db, email)
    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user