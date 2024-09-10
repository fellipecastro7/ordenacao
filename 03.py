import sys

def processaMedalhas():
    input = sys.stdin.read
    dado = input().splitlines()
    tabelaMedalhas = {}
    i = 0

    while i < len(dado):
        ouro = dado[i + 1]
        prata = dado[i + 2]
        bronze = dado[i + 3]

        if ouro not in tabelaMedalhas:
            tabelaMedalhas[ouro] = [0, 0, 0]

        tabelaMedalhas[ouro][0] += 1

        if prata not in tabelaMedalhas:
            tabelaMedalhas[prata] = [0, 0, 0]

        tabelaMedalhas[prata][1] += 1

        if bronze not in tabelaMedalhas:
            tabelaMedalhas[bronze] = [0, 0, 0]

        tabelaMedalhas[bronze][2] += 1

        i += 4

    listaMedalhas = [(pais, medalhas[0], medalhas[1], medalhas[2]) for pais, medalhas in tabelaMedalhas.items()]


    def compara(c1, c2):
        if c1[1] > c2[1]:
            return True
        
        if c1[1] < c2[1]:
            return False
        
        if c1[2] > c2[2]:
            return True
        
        if c1[2] < c2[2]:
            return False
        
        if c1[3] > c2[3]:
            return True
        
        if c1[3] < c2[3]:
            return False
        
        return c1[0] < c2[0]


    def mergeSort(lista):
        if len(lista) > 1:
            meio = len(lista) // 2
            esquerda = lista[:meio]
            direita = lista[meio:]

            mergeSort(esquerda)
            mergeSort(direita)

            i = j = k = 0

            while i < len(esquerda) and j < len(direita):
                if compara(esquerda[i], direita[j]):
                    lista[k] = esquerda[i]
                    i += 1

                else:
                    lista[k] = direita[j]
                    j += 1

                k += 1

            while i < len(esquerda):
                lista[k] = esquerda[i]
                i += 1
                k += 1

            while j < len(direita):
                lista[k] = direita[j]
                j += 1
                k += 1


    mergeSort(listaMedalhas)

    print("Quadro de Medalhas")

    for pais, ouro, prata, bronze in listaMedalhas:
        print(f"{pais} {ouro} {prata} {bronze}")


processaMedalhas()
