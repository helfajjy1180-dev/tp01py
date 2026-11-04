class Article:
    
    
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock
#methode pour calculer la valeur totale du stock
    def valeur_stock(self) -> float:
        """Calcule la valeur totale du stock en HT."""
        return self.prix_ht * self.stock
# methode pour ajouter du stock
    def ajouter_stock(self, quantite: int):
        """Ajoute une quantité au stock actuel."""
        if quantite < 0:
            raise ValueError("La quantité ajoutée ne peut pas être négative.")
        self.stock += quantite

    def __str__(self):
        return f"[{self.reference}] {self.designation} - Stock: {self.stock} - Prix HT: {self.prix_ht:.2f}€"

#exemple de test
a1 = Article("REF-001", "Clavier Mécanique", 89.99, 10)
print(a1.valeur_stock()) # 899.9
a1.ajouter_stock(5)
print(a1) # [REF-001] Clavier Mécanique - Stock: 15 - Prix HT: 89.99€

