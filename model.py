class Produit:
    code = ""
    nom = ""
    voix_admission = ""
    poso = ""
    categorie = ""
    origine = ""
    prix = ""
    quantite = ""

    def __init__(self, code, nom, voix_admission, poso, categorire, origine, prix,
                 quantite):
        self.code = code
        self.nom = nom
        self.voix_admission = voix_admission
        self.poso = poso
        self.categorie = categorire
        self.origine = origine
        self.prix = prix
        self.quantite = quantite

    def get_list(self):
        return {
            "code": self.code, "nom": self.nom, "voix_admission": self.voix_admission, "poso": self.poso,
            "categorie": self.categorie,
            "origine": self.origine, "prix": self.prix, "quantite": self.quantite
        }
