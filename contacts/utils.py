class WeakPasswordError(Exception):
    pass


def strong_password(password: str) -> bool:
    if len(password) < 8:
        raise WeakPasswordError("Too short")

    if not any(c.isupper() for c in password):
        raise WeakPasswordError("Missing uppercase letter")

    if not any(c.isdigit() for c in password):
        raise WeakPasswordError("Missing digit")

    if not any(c in "!@#$%^&*" for c in password):
        raise WeakPasswordError("Missing special character")

    return True
