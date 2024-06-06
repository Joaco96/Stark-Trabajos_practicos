from utils import *

def imprimir_campo(lista_sh: list, campo: str):
  map(lambda sh: print(sh[campo]), lista_sh)

def filtrar_valor_campo(lista_sh: list, campo: str, valor: str):
  return filter(lambda sh: sh[campo] == valor, lista_sh)

def calcular_mayor(lista_sh: list, campo: str):
  return custom_reduce(lambda ant, act: ant if float(ant[campo]) > float(act[campo]) else act, lista_sh)

def calcular_menor(lista_sh: list, campo: str):
  return custom_reduce(lambda ant, act: ant if float(ant[campo]) < float(act[campo]) else act, lista_sh)

def calcular_promedio(lista_sh: list, campo: str):
  floats_list = map(lambda sh: float(sh[campo]), lista_sh)
  return custom_reduce(lambda ant, act: ant + act, floats_list)

def reductora_cantidades(ant: dict, act: dict, campo: str):
  if(act[campo] == ""):
    ant["No Tiene"] = ant["No Tiene"] + 1
  else:
    ant[act[campo]] = ant[act[campo]] + 1
  return ant

def calcular_cantidades_campo(lista_sh: list, campo: str):
  maped_set = list(set(map(lambda sh: sh[campo] if sh[campo] != "" else "No Tiene", lista_sh)))
  initial_reduce_value = {}
  for item in maped_set:
    initial_reduce_value[item] = 0
  cantidades = custom_reduce(lambda ant, act: reductora_cantidades(ant, act, campo), lista_sh, initial_reduce_value)
  return cantidades

def reductora_shs(ant: list, act: dict, campo: str):
  if(act[campo] == ""):
    ant["No Tiene"].append(act["nombre"])
  else:
    ant[act[campo]].append(act["nombre"])
  return ant

def calcular_shs(lista_sh: list, campo: str):
  maped_set = list(set(map(lambda sh: sh[campo] if sh[campo] != "" else "No Tiene", lista_sh)))
  valor_inicial = {}
  for item in maped_set:
    valor_inicial[item] = []
  cantidades = custom_reduce(lambda ant, act: reductora_shs(ant, act, campo), lista_sh, valor_inicial)
  return cantidades