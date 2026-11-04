import functools

def valider_positif(*indices: int):
    """Décorateur qui valide que les arguments aux indices donnés sont positifs."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for idx in indices:
                if idx < len(args):
                    value = args[idx]
                    if not isinstance(value, (int, float)) or value <= 0:
                        raise ValueError(f"L'argument à l'index {idx} doit être un nombre positif.")
            return func(*args, **kwargs)
        return wrapper
    return decorator
#Application à une classe
class Rectangle:
    def __init__(self, largeur: float, hauteur: float):
        self.largeur = largeur
        self.hauteur = hauteur

    @valider_positif(1, 2) # Valide largeur (index 1) et hauteur (index 2)
    def aire(self, facteur: float = 1.0) -> float:
        return self.largeur * self.hauteur * facteur


 #Test
rect = Rectangle(5, 10)
print(rect.aire()) # 50.0

try:
    rect.aire(-1) # Doit lever une exception
except ValueError as e:
    print(e) # L'argument à l'index 1 doit être un nombre positif.

