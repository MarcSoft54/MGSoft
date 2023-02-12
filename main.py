from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView
import mysql.connector
from model import *

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="657284175",
#     database="pharmacie",
#     port="3305"
# )
#
# base_donnee = mydb.cursor()


class Liste_Medoc(BoxLayout):
    code = NumericProperty()
    nom = StringProperty()
    voix_admission = StringProperty()
    poso = StringProperty()
    categorie = StringProperty()
    origine = StringProperty()
    prix = NumericProperty()
    quantite = NumericProperty()


class MainWidget(Widget):
    ListeMedoc = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.produit = [
            Produit(2563, "paracytamol", "orale", "matin/soir", "preventive", "biologique", 1500, 25),
            Produit(2564, "paramol", "orale", "matin/soir", "preventive", "biologique", 100, 24),
            Produit(2565, "pytamol", "orale", "matin/soir", "preventive", "biologique", 150, 20)
        ]

    def on_parent(self, widget, parent):
        self.recycleView.data = [
            Produit.get_list() for Produit in self.produit
        ]


class MonApp(App):
    pass


MonApp().run()
