cor = {'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m',
       'azul': '\033[34m', 'lilás': '\033[35m', 'azul-claro': '\033[36m',
       'cinza': '\033[37m', 'branco':'\033[30m'}

fundo = {'vermelho':'\033[41m', 'verde':'\033[42m', 'amarelo':'\033[43m',
       'azul': '\033[44m', 'lilás': '\033[45m', 'azul-claro': '\033[46m',
       'cinza': '\033[47m', 'branco':'\033[30m'}

def cores(msg, c, f):
    """ Função que formata um texto com cor de texto e cor de fundo. As cores disponíveis para o texto e fundo são:
    Vermelho, verde, amarelo, azul, lilás, azul-claro, cinza e branco.
    Exemplo de uso da função: print(cores(texto, 'vermelho', 'amarelo')) >> texto terá fonte vermelha e fundo amarelo.

    :param msg: Mensagem a ser formatada.
    :param c: Cor do texto.
    :param f: Fundo do texto
    :return: Retorna o texto formatado.
    """
    return f'{cor[c]}{fundo[f]}{msg}\033[m'


# Main Program:
n = str(input('Digite a mensagem: '))
print(cores(n,'amarelo','azul'))
