from dataclasses import dataclass, field
from typing import List
@dataclass
class Produit:
    nom: str
    prix: float
    quantite: int = 0
    tags: List[str] = field(default_factory=list)

    def valeur_totale(self) -> float:
        return self.prix * self.quantite

#Exemple d'utilisation
p1 = Produit("Café", 5.5, 10, ["boisson", "chaud"])
p2 = Produit("Café", 5.5, 10, ["boisson", "chaud"])

print(p1) # Produit(nom='Café', prix=5.5, quantite=10, tags=['boisson', 'chaud'])
print(p1 == p2) # True
print(p1.valeur_totale()) # 55.0

# Modification de la liste par défaut (sécurisée)
p3 = Produit("Thé", 3.0)
print(p3.tags) # []