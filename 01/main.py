from data_stark import lista_personajes
from funciones_stark_mostrar import *

def desplegar_menu():
    print(f"\n-----")
    print(f"MENU STARK 01")
    print(f"-----")
    print(f"1. Nombres de superheroes masculinos")
    print(f"2. Nombres de superheroes femeninos")
    print(f"3. Superheroe mas alto masculino")
    print(f"4. Superheroe mas alto femenino")
    print(f"5. Superheroe mas bajo masculino")
    print(f"6. Superheroe mas bajo femenino")
    print(f"7. Altura promedio de los superheroes masculinos")
    print(f"8. Altura promedio de los superheroes femeninos")
    print(f"9. Nombres de superheroes 3 a 6")
    print(f"10. Cantidad de Superheroes por color de ojos")
    print(f"11. Cantidad de Superheroes por color de pelo")
    print(f"12. Cantidad de Superheroes por inteligencia")
    print(f"13. Superheroes por color de ojos")
    print(f"14. Superheroes por color de pelo")
    print(f"15. Superheroes por  inteligencia")
    print(f"\nx. Salir del programa")

def main():
    while True:
        desplegar_menu()
        eleccion = input("\n- Seleccionar una opción: ")
        match eleccion:
            case "1":
                mostrar_nombres_filtrado(lista_personajes, "genero", "M")
            case "2":
                mostrar_nombres_filtrado(lista_personajes, "genero", "F")
            case "3":
                mostrar_mas_alto_filtrado(lista_personajes, "genero", "M")
            case "4":
                mostrar_mas_alto_filtrado(lista_personajes, "genero", "F")
            case "5":
                mostrar_mas_bajo_filtrado(lista_personajes, "genero", "M")
            case "6":
                mostrar_mas_bajo_filtrado(lista_personajes, "genero", "F")
            case "7":
                mostrar_promedio_altura_filtrado(lista_personajes, "genero", "M")
            case "8":
                mostrar_promedio_altura_filtrado(lista_personajes, "genero", "F")
            case "9":
                mostrar_mas_alto_filtrado(lista_personajes, "genero", "M")
                mostrar_mas_alto_filtrado(lista_personajes, "genero", "F")
                mostrar_mas_bajo_filtrado(lista_personajes, "genero", "M")
                mostrar_mas_bajo_filtrado(lista_personajes, "genero", "F")
            case "10":
                mostrar_cantidad_por_campo(lista_personajes, "color_ojos", "con cada color de ojos")
            case "11":
                mostrar_cantidad_por_campo(lista_personajes, "color_pelo", "con cada color de pelo")
            case "12":
                mostrar_cantidad_por_campo(lista_personajes, "inteligencia", "con cada valor de inteligencia")
            case "13":
                mostrar_shs_por_campo(lista_personajes, "color_ojos", "con cada color de ojos")
            case "14":
                mostrar_shs_por_campo(lista_personajes, "color_pelo", "con cada color de pelo")
            case "15":
                mostrar_shs_por_campo(lista_personajes, "inteligencia", "con cada valor de inteligencia")
            case "x":
                return False

main()