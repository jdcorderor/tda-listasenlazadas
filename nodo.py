"""
    Tarea III: Listas enlazadas y TDA.
    Desarrollado por: Juan Diego Cordero y Nelson Guerrero.
"""

class Nodo:
    def __init__(self, valor: int):
        """
        Constructor de la Clase Nodo. Recibe como parámetro el contenido del nodo, que será guardado en el atributo valor. Además inicializa los atributos 'anterior' y 'siguiente' como None
        """
        self.valor = valor
        self.anterior = None
        self.siguiente = None