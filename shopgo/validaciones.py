def validar_password(password: str) -> bool :
    if not isinstance(password, str):
        return False
    if not 8 <= len(password) <= 20:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if any(char.isspace() for char in password):
        return False
    return True

def calcular_envio(subtotal: float) -> int:
    if subtotal < 0:
        raise ValueError("subtotal negativo")
    if subtotal >= 25000:
        return 0
    return 2500