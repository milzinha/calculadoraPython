# ..........CALCULADORA SIMPLES (super comentada)..........

# Olá, meu nome é Camila Carvalho e você deve ter obtido este código pelo meu perfil no GitHub (https://github.com/milzinha/milzinha)
# O objetivo desta calculadora é ajudar estudantes que querem entender o passo a passo de um programa simples, sem
# ter que sair pesquisando o significado de cada linha de código.

# ----------------DESCRIÇÃO DO PROGRAMA----------------

# 1- O usuário deve escolher um número de 1 a 4 para definfir que operação ele deseja fazer (Adição, Subtração, Multiplicação ou Divisão)
# 2- Então, ele digita dois números e o resultado será mostrado na tela.
# 3- Ele é questionado se quer sair do programa. Caso responda sim, o programa fecha, mas caso responda qualquer outra coisa, o programa executa tudo novamente desde o início.

# ==================INÍCIO DO PROGRAMA==================


# Primeiro, importamos a função sys, necessária para perguntar ao usuário se ele quer sair.
# Sem isso, o programa simplesmente fecharia ao terminar de executar o código apenas uma vez.
import sys

# A função main() é responsável por rodar o programa. Ou seja, tudo vai ser executado dentro dela.


def main():

    # Abaixo temos as funções: somar, subtrair, multiplicar e dividir. Dependendo do que o usuário escolher,
    # uma delas será executada por vez.
    # Observe que quando elas receberem os parâmetros x e y (representados pelos números que o usuários vão digitar),
    # elas retornarão uma operação.
    def somar(x, y):
        return x + y

    def subtrair(x, y):
        return x - y

    def multiplicar(x, y):
        return x * y

    def dividir(x, y):
        return x / y

    # Aqui temos um dicionário. Isso significa que quando a chave 1 for acionada, por exemplo, a função somar () será executada.
    operacoes = {
        1: somar,
        2: subtrair,
        3: multiplicar,
        4: dividir
    }

    # Agora temos um laço "while True:", ou seja, "Enquanto for verdade, execute:" Significa que o código será executado indefinidamente,
    # a não ser que seja interrompido por uma instrução break.
    while True:
        print("Selecione o número que corresponde à operação que deseja fazer:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")

        # Vamos agora tratar das exceções. Em outras palavras, como o programa vai ser comportar se o usuário digitar algo que seja diferente de um número entre 1 e 4.
        # No caso de uma exceção ValueError ou KeyError, o código imprime uma mensagem de erro e continua o laço.
        try:
            opcao = int(input("Digite sua opção: "))

        # Trata da exceção quando o usuário digita um caractere que não é um número inteiro (quando ele digita uma letra, por exemplo).
        except ValueError:
            print("Você não digitou um número. Por favor, digite um número entre 1 e 4:")
            continue

        # Com o método get(), utilizamos o dicionário operacoes para obter a função correspondente à operação selecionada. Por exemplo, se o usuário digitar 1, o código obterá a função soma().
        # Caso a chave não exista, o método get() retornará o valor padrão, que é None.
        resultado = operacoes.get(opcao, None)

        if resultado is None:
            # Trata da exceção quando o usuário digita um número, mas que não está entre 1 e 4, ou seja, não corresponde a nenhuma chave do dicionário.
            print("Opção inválida. Digite um número entre 1 e 4:")
            continue

        # Agora que as exceções para a escolha do tipo de operação foram tratadas, vamos chamar a função resultado.
        # A função resultado tem dois argumentos: o primeiro número e o segundo número. Ela retornará o resultado da operação matemática correspondente à opção selecionada pelo usuário.
        # Exemplo: se o usuário selecionar a opção 1, a função resultado() se tornará a função soma(). Se ele escolher a opção 2, a função resultado() será a função subtracao(). E assim por diante.
        resultado = resultado(float(input("Informe o primeiro número: ")), float(
            input("Informe o segundo número: ")))

        # Imprime na tela o resultado da operação.
        print("O resultado é:", resultado)

        # Pergunta se o usuário deseja sair ou rodar novamente as instruções.
        resposta = input("Deseja sair? (sim/não): ")

        # Se a resposta for "sim", o programa encerra. Caso ele responda qualquer outra coisa, o programa volta para o início.
        if resposta == "sim":
            sys.exit()


# Essa última parte é uma boa prática em scripts Python, para ajudar a manter o código organizado e evitar erros.
# Esse bloco é utilizado para garantir que o script seja executado apenas quando for o programa principal. Ou seja, quando estiver dentro da função main definida lá em cima.
# Isso evita que funções e classes sejam definidas em um módulo e, em seguida, executadas quando o módulo é importado por outro módulo.
if __name__ == "__main__":
    main()

# ==================FIM DO PROGRAMA==================

# Sabemos que há diversas formas de resolver o mesmo problema.
# Como você melhoraria este código?

# Você deve ter percebido que eu não tratei das exceções caso o usuário informe algum caractere que não seja um número (lá na funcão resultado).
# Como você resolveria essas exceções?

# Espero que este código ajude a quem estiver iniciando em Python.

# BONS ESTUDOS! :)
