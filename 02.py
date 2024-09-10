def quickSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio < fim:
        p = partition(lista, inicio, fim)
        quickSort(lista, inicio, p - 1)
        quickSort(lista, p + 1, fim)


def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio

    for j in range(inicio, fim):
        if comparaPaises(lista[j], pivot):
            lista[i], lista[j] = lista[j], lista[i]
            i += 1

    lista[i], lista[fim] = lista[fim], lista[i]
    return i


def comparaPaises(p1, p2):
    if p1[1] > p2[1]:
        return True
    
    if p1[1] < p2[1]:
        return False
    
    if p1[2] > p2[2]:
        return True
    
    if p1[2] < p2[2]:
        return False
    
    if p1[3] > p2[3]:
        return True
    
    if p1[3] < p2[3]:
        return False

    return p1[0] < p2[0]


n = int(input())
paises = []

for _ in range(n):
    dadosPais = input().split()
    pais = dadosPais[0]
    ouro = int(dadosPais[1])
    prata = int(dadosPais[2])
    bronze = int(dadosPais[3])
    paises.append((pais, ouro, prata, bronze))

quickSort(paises)

for pais in paises:
    print(f'{pais[0]} {pais[1]} {pais[2]} {pais[3]}')
