"""
    PEP8 - Python Enhancement Proposal
    The Zen of Python: import this.

    A ideia da PEP8 é que possamos escrever código Python de forma Pyathônica.

    [1] - Utilize Camel Case para nomes de classes;

        class Calculadora:
        pass


        class CalculadoraCientifica:
            pass

    [2] - Utilizer nomes em minusculos, seprados por underline para funções ou variaveis;

        def soma():
            pass


        def soma_dois():
            pass

        numero = 4

        numero_impar = 5
    [3] - Utilizer 4 espaço para a identação! (Não use tab)

        if 'a' in 'banana':
            print('tem')

    [4] - Linhas em branco
     - Separar funções e definições de classes com 2 linhas em branco;
     - Métodos dentro de uma classe devem ser separados com uma única linha em branco;

    [5] - Imports devem ser sempre feitos em linhas  seaparadas
        # Import Errado
        import sys, os

        # Import Certo

        import sys
        import os

        # Não há problema em utilizar:
        from types import StringTypes, ListTypes

        # Caso tenha muito imports de um mesmo pacote, recomenda-se fazer:

        from types import (
            StringType,
            ListType,
            SetType,
            OutroType
        )
         # Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou doctrings e
         # antes constantes ou variaveis globais.

    [6] - Espaço em expressões e instruções;
        # Não faça

        funcao(_algo[_1_], {_outro: 2_}_)

        # Faça
        funcao(algo[1], {outro: 2})

        # Não faça
        algo_(1)

        # Faça:
        algo(1)

        # Não faça

        dict_['chave'] = list_[indice]

        # Faça

        dict['chave'] = list[indice]

        # Não faça
        x              = 1
        y              = 3
        variavel_longa = 5

        # Faça
        x = 1
        y = 3
        variavel_longa = 5

    [7] - Termine sempre uma instrução com uma nova linha;
"""
import this
