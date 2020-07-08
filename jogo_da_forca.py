from random import randint
from unicodedata import normalize


def remover_acentos(string):
    """Recebe uma string e retorna a versão dela sem acentos ortográficos e em lowercase."""
    normalizado = normalize('NFD', string)
    return normalizado.encode('ascii', 'ignore').decode('utf8').lower()


def validar_entrada(string):
    """Recebe uma string e retorna True se ela tiver 1 caractere."""
    return len(string) == 1


def obter_palavra():
    """Abre um arquivo com as palavras, armazena em uma lista; obtém um número aleatório de 0 a x, onde x é o número
    de itens da lista; e usa esse número para escolher e retornar uma palavra aleatória da lista."""
    arquivo = open('palavras_faceis.txt', 'r', encoding='UTF-8')
    lista_de_palavras = arquivo.read().split('\n')
    arquivo.close()
    sorteio = randint(0, len(lista_de_palavras))
    return lista_de_palavras[sorteio]


def main():
    palavra = obter_palavra()
    parcial = "_" * len(palavra)  # cria uma string de "_" do tamanho da palavra
    n_tentativas = 0
    erros = ""
    while True:
        entrada = input("-- Entre com uma letra --> ").lower()
        if validar_entrada(entrada):  # se a entrada for válida
            n_tentativas += 1
            palavra_normalizada = remover_acentos(palavra)
            print(f"A palavra é: {palavra}")  # Debug
            print(f"A letra aparece {palavra_normalizada.count(entrada)} vezes")
            print(f"Tentativas = {n_tentativas}")

            if remover_acentos(entrada) not in palavra.lower():
                erros += entrada + " "

            contador = 0
            for letra in palavra:
                if remover_acentos(letra) == entrada:  # se o jogador acertou a letra
                    parcial_lista = list(parcial)  # converte parcial para lista
                    parcial_lista[contador] = letra  # substitui a letra na lista
                    parcial = "".join(parcial_lista)  # converte a lista de volta para string

                contador += 1  # adiciona 1 ao contador

        print('\n')
        print(parcial)
        print(f"Erros: {erros.upper()}")

        if "_" not in parcial:
            print("Game Over\nParabéns!")
            break


if __name__ == "__main__":
    main()
