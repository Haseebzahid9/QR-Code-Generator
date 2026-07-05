import re
from urllib.parse import urlparse


def validate_nonempty(s: str) -> bool:
    return bool(s and s.strip())


def validate_url(url: str) -> bool:
    try:
        p = urlparse(url)
        return p.scheme in ("http", "https") and bool(p.netloc)
    except Exception:
        return False


def validate_email(email: str) -> bool:
    if not email:
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def validate_phone(phone: str) -> bool:
    if not phone:
        return False
    # Basic international phone validation (allows + and digits, min 7 digits)
    pattern = r"^\+?[0-9\- ]{7,}$"
    return re.match(pattern, phone) is not None
