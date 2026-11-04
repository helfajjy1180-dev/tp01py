class Contact:
    def __init__(self, nom: str, telephone: str, email: str):
        self.nom = nom
        self.telephone = telephone
        self.email = email

    @property
    def initiale(self):
        """Retourne la première lettre du nom en majuscule."""
        return self.nom[0].upper() if self.nom else ""

    def __repr__(self):
        return f"Contact(nom='{self.nom}', email='{self.email}')"

#definition de la classe Carnet pour gérer une collection de contacts

class Carnet:
    def __init__(self):
        self.contacts = []

    def ajouter(self, contact: Contact):
        self.contacts.append(contact)

    def chercher(self, nom_partiel: str) -> list:
        """Retourne la liste des contacts dont le nom contient la chaîne donnée."""
        nom_partiel_lower = nom_partiel.lower()
        return [c for c in self.contacts if nom_partiel_lower in c.nom.lower()]

    def __len__(self):
        return len(self.contacts)

#Test complet des clases Contact et Carnet
carnet = Carnet()
c1 = Contact("Alice Dupont", "0612345678", "alice@example.com")
c2 = Contact("Bob Martin", "0698765432", "bob@example.com")
carnet.ajouter(c1)
carnet.ajouter(c2)

print(c1.initiale) # A
resultats = carnet.chercher("ali")
print(resultats) # [Contact(nom='Alice Dupont', email='alice@example.com')]
print(len(carnet)) # 2


