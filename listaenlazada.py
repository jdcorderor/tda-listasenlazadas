"""
    Tarea III: Listas enlazadas y TDA.
    Desarrollado por: Juan Diego Cordero y Nelson Guerrero.
"""

from nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.nodocabeza = None

    def menu(self, band = True):
        while band:
            print("\n\n------------------ Menú de opciones ------------------")
            print("1. Insertar un nodo en una posición de la lista enlazada.")
            print("2. Eliminar un nodo de la lista enlazada.")
            print("3. Revertir la lista enlazada.")
            print("4. Eliminar duplicados de la lista enlazada.")
            print("5. Buscar un valor en la lista enlazada.")
            print("6. Mostrar por consola la lista enlazada.")
            print("7. Salir.")
            try:
                opcion = int(input("\nEstimado usuario, ingrese una opción: "))
            except ValueError:
                print("\n--- Opción no válida. Intente de nuevo.")
                continue
            if opcion == 1:
                try:
                    index = int(input("\nIngrese la posición en que desea insertar el nodo: "))
                    valor = int(input("Ingrese el valor entero del nodo: "))
                except ValueError:
                    print("\n--- Valores no válidos. Intente de nuevo.")
                self.insertar_nodo(index, valor)
            elif opcion == 2:
                if self.nodocabeza is None:
                    print("\n--- Error. Lista doblemente enlazada vacía.")
                    continue
                print("0. Eliminar un nodo por su posición.")
                print("1. Eliminar un nodo por su valor.")
                try:
                    subopcion = int(input("\nIngrese la opción que desea utilizar: "))
                except ValueError:
                    print("\n--- Opción no válida. Intente de nuevo.")
                    continue
                if subopcion == 0:
                    try:
                        index = int(input("\nIngrese la posición del nodo que desea eliminar: "))
                    except ValueError:
                        print("\n--- Índice no válido. Intente de nuevo.")
                        continue
                    self.eliminar_nodo(index, None)
                elif subopcion == 1:
                    try:
                        valor = int(input("\nIngrese el valor del nodo que desea eliminar: "))
                    except ValueError:
                        print("\n--- Valor no válido. Intente de nuevo.")
                        continue
                    self.eliminar_nodo(None, valor)
                else:
                    print("\n--- Opción no válida. Intente de nuevo.")
                    continue
            elif opcion == 3:
                self.revertir_lista()
            elif opcion == 4:
                self.eliminar_duplicados()
            elif opcion == 5:
                if self.nodocabeza is None:
                    print("\n--- Error. Lista doblemente enlazada vacía.")
                    continue
                try:
                    valor = int(input("\nIngrese el valor entero que desea buscar: "))
                except ValueError:
                    print("\n--- Opción no válida. Intente de nuevo.")
                    continue
                posiciones = self.buscar_nodo(valor)
                if len(posiciones) > 0:
                    print(f"\nPosición(es) del valor {valor} en la lista doblemente enlazada:", end=" ")
                    print(", ".join(posiciones))
                else:
                    print(f"\n--- Error. Valor {valor} no encontrado en la lista doblemente enlazada.")
            elif opcion == 6:
                self.mostrar_lista()
            elif opcion == 7:
                band = False
            else:
                print("\n--- Opción no válida. Intente de nuevo.")

    def insertar_nodo(self, posicion: int, valor: int):
        nodo_nuevo = Nodo(valor)
        if posicion == 0:
            nodo_nuevo.siguiente = self.nodocabeza
            if self.nodocabeza is not None:
                self.nodocabeza.anterior = nodo_nuevo
            self.nodocabeza = nodo_nuevo
        else:
            actual = self.nodocabeza
            for _ in range(posicion):
                if actual is None:
                    print("\n--- Error. Posición fuera de rango.")
                    return
                anterior = actual
                actual = actual.siguiente
            nodo_nuevo.siguiente = actual
            nodo_nuevo.anterior = anterior
            if nodo_nuevo.siguiente is not None:
                nodo_nuevo.siguiente.anterior = nodo_nuevo
            anterior.siguiente = nodo_nuevo
        print(f"\nNodo con valor {valor} insertado en la posición {posicion}.")

    def eliminar_nodo(self, posicion: int, valor: int):
        if posicion is not None:
            if posicion == 0:
                if self.nodocabeza is None:
                    print("\n--- Error. Posición fuera de rango.")
                    return
                self.nodocabeza = self.nodocabeza.siguiente
                if self.nodocabeza is not None:
                    self.nodocabeza.anterior = None
            else:
                actual = self.nodocabeza
                for _ in range(posicion):
                    if actual is None:
                        print("\n--- Error. Posición fuera de rango.")
                        return
                    actual = actual.siguiente
                if actual is None:
                    print("\n--- Error. Posición fuera de rango.")
                    return
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
            print(f"\nNodo en la posición {posicion} eliminado.")
        elif valor is not None:
            i = 0
            actual = self.nodocabeza
            while actual is not None:
                if actual.valor == valor:
                    i += 1
                    if actual.anterior is not None:
                        actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente is not None:
                        actual.siguiente.anterior = actual.anterior
                    if actual == self.nodocabeza:
                        self.nodocabeza = actual.siguiente
                actual = actual.siguiente
            if i == 0:
                print("\n--- Error. Valor no encontrado en la lista doblemente enlazada.")
            else:
                print(f"\nNodo con valor {valor} eliminado.")

    def revertir_lista(self):
        if self.nodocabeza is None:
            print("\n--- Error. Lista doblemente enlazada vacía.")
            return
        actual = self.nodocabeza
        temporal = None
        while actual is not None:
            temporal = actual.anterior
            actual.anterior = actual.siguiente
            actual.siguiente = temporal
            actual = actual.anterior
        if temporal is not None:
            self.nodocabeza = temporal.anterior
        print("\nLista doblemente enlazada revertida.")

    def eliminar_duplicados(self):
        if self.nodocabeza is None:
            print("\n--- Error. Lista doblemente enlazada vacía.")
            return
        i = 0
        actual = self.nodocabeza
        while actual is not None:
            nodo_comparador = actual.siguiente
            while nodo_comparador is not None:
                if actual.valor == nodo_comparador.valor:
                    i += 1
                    if nodo_comparador.anterior is not None:
                        nodo_comparador.anterior.siguiente = nodo_comparador.siguiente
                    if nodo_comparador.siguiente is not None:
                        nodo_comparador.siguiente.anterior = nodo_comparador.anterior
                nodo_comparador = nodo_comparador.siguiente
            actual = actual.siguiente
        if i == 0:
            print("\n--- Error. No hay duplicados en la lista doblemente enlazada.")
        else:
            print("\nDuplicados eliminados de la lista doblemente enlazada.")

    def buscar_nodo(self, valor: int):
        if self.nodocabeza is None:
            print("\n--- Error. Lista doblemente enlazada vacía.")
            return
        posiciones = []
        actual = self.nodocabeza
        posicion = 0
        while actual is not None:
            if actual.valor == valor:
                posiciones.append(str(posicion))
            actual = actual.siguiente
            posicion += 1
        return posiciones

    def mostrar_lista(self):
        if self.nodocabeza != None:
            print("\n--- Lista doblemente enlazada\n")
            nodo = self.nodocabeza
            print(nodo.valor, end=" <-> ")
            while nodo.siguiente != None:
                nodo = nodo.siguiente
                print(nodo.valor, end=" <-> ")
            print("None")
        else:
            print("\n--- Error. Lista doblemente enlazada vacía.")