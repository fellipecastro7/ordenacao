def mergeSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)

    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        mergeSort(lista, inicio, meio)
        mergeSort(lista, meio, fim)
        merge(lista, inicio, meio, fim)


def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    topoEsquerda, topoDireita = 0, 0

    for k in range(inicio, fim):
        if topoEsquerda >= len(esquerda):
            lista[k] = direita[topoDireita]
            topoDireita += 1

        elif topoDireita >= len(direita):
            lista[k] = esquerda[topoEsquerda]
            topoEsquerda += 1

        elif esquerda[topoEsquerda] < direita[topoDireita]:
            lista[k] = esquerda[topoEsquerda]
            topoEsquerda += 1

        else:
            lista[k] = direita[topoDireita]
            topoDireita += 1


def imprimeAlunoSorteado(k, lista):
    mergeSort(lista)
    return lista[k - 1]


n, k = map(int, input().split())
nomes = []

for _ in range(n):
    nome = input().strip()
    nomes.append(nome)

print(imprimeAlunoSorteado(k, nomes))
