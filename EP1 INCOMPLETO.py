import random
import timeit
import sys
from time import process_time

sys.setrecursionlimit(80000)
Lista_apoio = random.sample(range(0, 14000), 2000)

def busca_sequencial(lista):
    a = len(lista) // 2
    for i in lista:
        if i == lista[a]:
            return lista.index(i)
    return 0

def busca_binaria(lista):
    x = len(lista) // 2
    d = len(lista) 
    e = -1
    m = 0
    while e < d - 1:
        m = (e+d)//2
        if lista[m] < x:
            e = m
        else:
            d = m
    return d

def insercao(lista):
    for ls in range(0,len(lista)):
        i = ls-1
        aux = lista[ls] 
        while(i >= 0) and (lista[i] > aux):
            lista[i+1] = lista[i]
            i = i-1
        lista[i+1] = aux
    return lista

def selecao(lista):
    for ls in range(len(lista)):
        aux = ls
        for k in range(ls+1, len(lista)):
            if lista[k] < lista[aux]:
                aux = k
        lista[ls] = lista[aux]
        lista[aux] = lista[ls]
    return lista  

def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivô = lista[0]
    iguais  = [x for x in lista if x == pivô]
    menores = [x for x in lista if x <  pivô]
    maiores = [x for x in lista if x >  pivô]
    return quicksort(menores) + iguais + quicksort(maiores)

def soma_tempo(func, parametro):
    t1 = process_time()
    func(parametro)
    return round(process_time()-t1,2)        
   
def main():
    resultados = []
    lista = [insercao, selecao, mergesort, quicksort]
    while len(Lista_apoio) <= 14000:
        resultados.append(len(Lista_apoio))
        for i in lista:
            resultados.append(soma_tempo(i,Lista_apoio))
        for a in lista:
            resultados.append(busca_binaria(Lista_apoio))
        print("              %d     %.2f     %.2f    %.2f   %.2f              %.2f  %.2f  %.2f %.2f  "
     %(resultados[0], resultados[1], resultados[2], resultados[3], resultados[4], resultados[5], resultados[6], resultados[7]
       ,resultados[8]))
        resultados = []
        Lista_apoio.extend(random.sample(range(0,10000),2000))
    return resultados
        

def verifica():
    while len(Lista_apoio) <= 24000:
        print(len(Lista_apoio))
        print(soma_tempo(quicksort,Lista_apoio))
        Lista_apoio.extend(random.sample(range(0,10000),2000))
        
def resultados():
    return'''|-------------------------[EP1 - Vale a pena ordenar?]------------------------------------------|
             |   Algoritmos escolhidos: Insercao Selecao Merge Quick       Duracao dos testes:               |
             |                                                                                               |
             |            Aluno: Gustavo Henrique de Oliveira                                                |
             |                                                                                               |
             |                     Tempos de Ordenacao               Numero de Buscas                        |
             |-----------------------------------------------------------------------------------------------|
             |   n   | Insercao Selecao  Merge  Quick         |    Insercao   Selecao  Merge   Quick         |
             |-----------------------------------------------------------------------------------------------|'''

print(resultados())
print(main())
