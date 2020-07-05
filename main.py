from random import randint
from unicodedata import normalize

# abre um arquivo com as palavras, armazena em uma string e converte para uma lista
arquivo = open('palavras_faceis.txt', 'r', encoding='UTF-8')
lista_de_palavras = arquivo.read().split('\n')
arquivo.close()

# obtém um número aleatório de 0 a x, onde x é o número de itens da lista;
sorteio = randint(0, len(lista_de_palavras))
# e usa esse número para escolher uma palavra aleatória da lista
palavra = lista_de_palavras[sorteio]
parcial = "_" * len(palavra)  # cria uma string de "_" do tamanho da palavra
tentativas = 0
letras_usadas = ''


def remover_acentos(string):
    normalizado = normalize('NFD', string)
    return normalizado.encode('ascii', 'ignore').decode('utf8').lower()


def validar_chute(string):
    tamanho = len(string)
    return tamanho == 1  # retorna True caso verdadeiro


while True:
    chute = input("-- Entre com uma letra --> ")
    if validar_chute(chute):  # se o chute for válido
        tentativas += 1
        letras_usadas += chute + ' '
        palavra_normalizada = remover_acentos(palavra)
        print("A letra aparece", palavra_normalizada.count(chute), "vezes")
        print('Tentativas =', tentativas)

        contagem = 0  # inicia um contador
        for letra in palavra:
            if remover_acentos(letra) == chute:
                parcial_lista = list(parcial)  # converte parcial para lista
                parcial_lista[contagem] = letra  # substitui a letra na lista
                parcial = ''.join(parcial_lista)  # converte a lista de volta para string
            contagem += 1  # adiciona 1 ao contador

    print('\n')
    print(parcial)
    print("Letras já usadas:", letras_usadas)

    if "_" not in parcial:
        print("Game Over\nParabéns!")
        break
