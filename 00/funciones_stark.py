from utils import *

def mostrar_nombres(lista_sh:list) -> None:
    print(f"\nNombres de cada superheroe")
    print(f"--------------------------")
    map(lambda sh: print(sh["nombre"]), lista_sh)

def mostrar_nombres_altura(lista_sh:list) -> None:
    print(f"\nNombres y altura de cada superheroe")
    print(f"----------------------------------")
    map(lambda sh: print(f"{sh["nombre"]} / {round(float(sh["altura"]),2)}cm"), lista_sh)

def superheroe_alto(lista_sh:list) -> None:
    print(f"\nSuperheroe mas alto")
    print(f"--------------------")
    sh_alto = custom_reduce(lambda ant, act: ant if float(ant["altura"]) > float(act["altura"]) else act, lista_sh)
    print(f"{sh_alto["nombre"]} / {round(float(sh_alto["altura"]),2)}cm")

def superheroe_bajo(lista_sh:list) -> None:
    print(f"\nSuperheroe mas bajo")
    print(f"--------------------")
    sh_bajo = custom_reduce(lambda ant, act: ant if float(ant["altura"]) < float(act["altura"]) else act, lista_sh)
    print(f"{sh_bajo["nombre"]} / {round(float(sh_bajo["altura"]),2)}cm")

def mostrar_altura_promedio(lista_sh:list) -> None:
    print(f"\nAltura promedio")
    print(f"---------------")
    alturas_float = map(lambda sh: float(sh["altura"]), lista_sh)
    sumatoria = custom_reduce(lambda ant, act: ant + act, alturas_float)
    print(f"{round(sumatoria/len(lista_sh),2)}cm")


def identidad_bajo_alto(lista_sh:list) -> None:
    print(f"\nIdentidad superheroe mas alto")
    print(f"--------------------")
    sh_alto = custom_reduce(lambda ant, act: ant if float(ant["altura"]) > float(act["altura"]) else act, lista_sh)
    print(f"{sh_alto["identidad"]}")
    print(f"\nIdentidad superheroe mas bajo")
    print(f"--------------------")
    sh_bajo = custom_reduce(lambda ant, act: ant if float(ant["altura"]) < float(act["altura"]) else act, lista_sh)
    print(f"{sh_bajo["identidad"]}")

def superheroe_pesado_liviano(lista_sh:list) -> None:
    print(f"\nSuperheroe mas pesado")
    print(f"--------------------")
    sh_pesado = custom_reduce(lambda ant, act: ant if float(ant["peso"]) > float(act["peso"]) else act, lista_sh)
    print(f"{sh_pesado["nombre"]} / {round(float(sh_pesado["peso"]),2)}kg")
    print(f"\nSuperheroe mas liviano")
    print(f"--------------------")
    sh_liviano = custom_reduce(lambda ant, act: ant if float(ant["peso"]) < float(act["peso"]) else act, lista_sh)
    print(f"{sh_liviano["nombre"]} / {round(float(sh_liviano["peso"]),2)}kg")






