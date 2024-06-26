import csv
from datetime import datetime
from Revista import Revista
import re
#Nombres: Gael Humberto Borchardt Castellanos Daniel Ivan Estrada Neri

def carga_csv(nombre_archivo:str)->list:
    '''
    Carga archivo csv y regresa una lista 
    '''
    lista = []
    with open(nombre_archivo,'r',encoding="utf-8") as archivo:
        lista = list(csv.DictReader(archivo))
    return lista


def crea_diccionario_revistas_por_cada_titulo(lista_revistas:list)->dict:
    ''' Crea diccionario de revistas a partir de 
        la lista de revistas
        {"id_revista" ={dict_revista}}
    '''
    d = {}
    for revista in lista_revistas:
        key = revista["titulo"]
        d[key] = revista # key,value
    return d

def crea_diccionario_alfabetico(lista_revistas:list)->dict:
    d = {}
    for revista in lista_revistas:
        letra = revista["titulo"][0].upper()
        if letra in d:
            d[letra].append(revista)
        else:
            d[letra] = [revista]
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    return d

def explorar_abcedario(dic_por_palabras:dict):
    d = {}
    for key,revistas in dic_por_palabras.items():
        letra = key[0].upper()
        if letra in d:
            d[letra].append({key:revistas})
        else:
            d[letra] = [{key:revistas}]
    return d

def Diccionario_Revistas_Por_Cada_Palabra(lista_Revista:list[Revista])->dict:
    diccionario={}
    for revista in lista_Revista:
        #revista=dict(revista)
        titulo=revista["titulo"]
        splitteado=titulo.split()
        for palabra in splitteado: 
            palabra_limpia = re.sub(r'[^a-zA-Z0-9]', '', palabra).lower()
            if palabra_limpia != "":
                if palabra_limpia in diccionario:
                    diccionario[palabra_limpia].append(revista)
                else:
                    diccionario[palabra_limpia]=[revista]
    return diccionario

def crear_diccionario_por_pais(lista_Revista)->dict:
    d={}
    for revista in lista_Revista:
        pais=revista["pais"]
        if pais in d:
            d[pais].append(revista)
        else:
            d[pais]=[revista]
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    return d

 

def Buscar_Revista(diccionario:dict, palabra:str)->list:
    lista=[]
    if palabra in diccionario:
       print("\n Revistas encontradas: ")
       for revista in diccionario[palabra]:
            print(f"{revista}")
            lista.append(revista)
    return lista

def ordenar_por_quartil(lista_revistas:list)->list:
    lista_revistas.sort(key=lambda revista: revista["q"])
    return lista_revistas

def diccionario_de_palabras_por_letras( dict_palabras:dict)->dict:
    # buscamos que los diccionarios de palabras esten dentro de las keys de cada letra
    d={}	
    for k,v in dict_palabras.items():
        letra=k[0].upper()
    
        if letra not in d:
            d[letra]=[v]
        else:
            d[letra].append(v)
        
    d={k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    return d #nos devuelve un diccionario de listas de diccionarios :P

def find_keys_containing_substring(dictionary, substring)->dict:
    matching_keys = {}
    for key in dictionary.keys():
        if substring in key:
            matching_keys[key] = dictionary[key]
    return matching_keys

if __name__ == '__main__':
    archivo = 'revistas.csv'
    catalogo = carga_csv(archivo)
    diccionario_revistas=Diccionario_Revistas_Por_Cada_Palabra(catalogo)
    # for k,v in diccionario_revistas.items():
    #     print(f"{k}\n:{v}\n")
    # lista_nueva = find_keys_containing_substring(diccionario_revistas,'atmos')
    # for key in lista_nueva.keys():
    #     revistas = lista_nueva[key]
    #     for revista in revistas:
    #         print(revista['titulo'])
    #dic_explorar = explorar_abcedario(diccionario_revistas)
    #for key in dic_explorar.keys():
    #    print(f'letra: {key}\n {dic_explorar[key]}')
    # diccionario_revistas_titulos=crea_diccionario_revistas_por_cada_titulo(catalogo)
    # diccionario_pais=crear_diccionario_por_pais(catalogo)
    # diccionario_alfabetico=crea_diccionario_alfabetico(catalogo) #los values del diccionario son listas de revistas
    # for k,v in diccionario_alfabetico.items():
    #     print(f"{k}\n:{v}\n")
    # dict_unido=diccionario_de_palabras_por_letras(diccionario_revistas)
    # for k,v in dict_unido.items():
    #     print(f"{k}\n:{v}\n")   
    dicc_paises=crear_diccionario_por_pais(catalogo)
    for k,v in dicc_paises.items():
        print(f"{k}\n:{v}\n")
        break