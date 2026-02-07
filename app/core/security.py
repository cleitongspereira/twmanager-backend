import hashlib
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _normalize_password(password: str) -> bytes:
    # remove espaços, quebras de linha e afins
    clean = password.strip().encode("utf-8")

    # pré-hash para eliminar limite de 72 bytes do bcrypt
    return hashlib.sha256(clean).digest()


def hash_password(password: str) -> str:
    normalized = _normalize_password(password)
    return pwd_context.hash(normalized)


def verify_password(password: str, password_hash: str) -> bool:
    normalized = _normalize_password(password)
    return pwd_context.verify(normalized, password_hash)