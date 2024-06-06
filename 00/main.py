from data_stark import lista_personajes
from funciones_stark import *

def desplegar_menu():
    print(f"\n-----")
    print(f"MENU STARK 00")
    print(f"-----")
    print(f"1. Nombres de cada superheroe")
    print(f"2. Nombres y altura de cada superheroe")
    print(f"3. Superheroe mas alto")
    print(f"4. Superheroe mas bajo")
    print(f"5. Altura promedio de los superheroes")
    print(f"6. Identidad de superheroe mas bajo y mas alto")
    print(f"7. Superheroe mas y menos pesado")
    print(f"\nx. Salir del programa")

def main():
    while True:
        desplegar_menu()
        eleccion = input("\n- Seleccionar una opción: ")
        match eleccion:
            case "1":
                mostrar_nombres(lista_personajes)
            case "2":
                mostrar_nombres_altura(lista_personajes)
            case "3":
                superheroe_alto(lista_personajes)
            case "4":
                superheroe_bajo(lista_personajes)
            case "5":
                mostrar_altura_promedio(lista_personajes)
            case "6":
                identidad_bajo_alto(lista_personajes)
            case "7":
                superheroe_pesado_liviano(lista_personajes)
            case "x":
                return False

main()