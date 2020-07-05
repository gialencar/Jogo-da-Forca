from random import randint
from unicodedata import normalize


def remover_acentos(string):
    normalizado = normalize('NFD', string)
    return normalizado.encode('ascii', 'ignore').decode('utf8').lower()


def validar_chute(string):
    # Retorna True se a string tiver 1 caractere
    return len(string) == 1


# abre um arquivo com as palavras, armazena em uma string e converte para uma lista TODO: escolha de nível
arquivo = open('palavras_faceis.txt', 'r', encoding='UTF-8')
lista_de_palavras = arquivo.read().split('\n')
arquivo.close()

# obtém um número aleatório de 0 a x, onde x é o número de itens da lista;
sorteio = randint(0, len(lista_de_palavras))
# e usa esse número para escolher uma palavra aleatória da lista
palavra = lista_de_palavras[sorteio]
parcial = "_" * len(palavra)  # cria uma string de "_" do tamanho da palavra
n_tentativas = 0
letras_usadas = ""

while True:
    chute = input("-- Entre com uma letra --> ")
    if validar_chute(chute):  # se o chute for válido
        n_tentativas += 1
        letras_usadas += chute + " "
        palavra_normalizada = remover_acentos(palavra)
        print(f"A letra aparece {palavra_normalizada.count(chute)} vezes")
        print(f"Tentativas = {n_tentativas}")

        contador = 0
        for letra in palavra:
            if remover_acentos(letra) == chute:
                parcial_lista = list(parcial)  # converte parcial para lista
                parcial_lista[contador] = letra  # substitui a letra na lista
                parcial = "".join(parcial_lista)  # converte a lista de volta para string
            contador += 1  # adiciona 1 ao contador

    print('\n')
    print(parcial)
    print(f"Letras já usadas: {letras_usadas.upper()}")

    if "_" not in parcial:
        print("Game Over\nParabéns!")
        break
