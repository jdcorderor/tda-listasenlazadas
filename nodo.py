"""
    Tarea III: Listas enlazadas y TDA.
    Desarrollado por: Juan Diego Cordero y Nelson Guerrero.
"""

class Nodo:
    def __init__(self, valor: int):
        self.valor = valor
        self.anterior = None
        self.siguiente = None