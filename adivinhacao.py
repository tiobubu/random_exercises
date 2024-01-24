import random

def jogo_adivinhacao():
    numale = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativa = int(input('Tente adivinhar o número entre 1 e 100: '))
        tentativas += 1

        if tentativa < numale: print('Tente um número maior.')
        elif tentativa > numale: print('Tente um número menor.')
        else:
            print(f'Parabéns! Você acertou o número {numale} em {tentativas} tentativas')
            break

if __name__ == '__main__':
    jogo_adivinhacao()

# alteração feita