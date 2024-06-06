from funciones_stark_calcular import *

def mostrar_nombres_filtrado(lista_sh: list, campo_filtro: str, valor_filtro: str) -> None:
    print(f"\nNombres de superheroes {valor_filtro}")
    print(f"--------------------")
    filtered_list = filtrar_valor_campo(lista_sh, campo_filtro, valor_filtro)
    imprimir_campo(filtered_list, "nombre")

def mostrar_mas_alto_filtrado(lista_sh: list, campo_filtro: str, valor_filtro: str) -> None:
    print(f"\nSuperheroe mas alto {valor_filtro}")
    print(f"--------------------")
    filtered_list = filtrar_valor_campo(lista_sh, campo_filtro, valor_filtro)
    mas_alto = calcular_mayor(filtered_list, "altura")
    print(f'{mas_alto["nombre"]} / {round(float(mas_alto["altura"]),2)}')

def mostrar_mas_bajo_filtrado(lista_sh: list, campo_filtro: str, valor_filtro: str) -> None:
    print(f"\nSuperheroe mas bajo {valor_filtro}")
    print(f"--------------------")
    filtered_list = filtrar_valor_campo(lista_sh, campo_filtro, valor_filtro)
    mas_bajo = calcular_menor(filtered_list, "altura")
    print(f'{mas_bajo["nombre"]} / {round(float(mas_bajo["altura"]),2)}')

def mostrar_promedio_altura_filtrado(lista_sh: list, campo_filtro: str, valor_filtro: str) -> None:
    print(f"\nAltura promedio de los superheroes {valor_filtro}")
    print(f"--------------------")
    filtered_list = filtrar_valor_campo(lista_sh, campo_filtro, valor_filtro)
    promedio = calcular_promedio(filtered_list, "altura")
    print(f"{round(promedio/len(filtered_list),2)}")


def mostrar_cantidad_por_campo(lista_sh:list, campo: str, filtro: str) -> None:
    print(f"\nCantidad de Superheroes {filtro}")
    print(f"--------------------")
    elementos = calcular_cantidades_campo(lista_sh, campo)
    for key, value in elementos.items():
        print(f"{key} :  {value}")

def mostrar_shs_por_campo(lista_sh:list, campo: str, filtro: str) -> None:
    print(f"\nSuperheroes {filtro}")
    print(f"--------------------")
    elementos = calcular_shs(lista_sh, campo)
    for key, value in elementos.items():
        print(f"{key} :  {value}")








