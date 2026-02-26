"""
Calculadora simples em Python
Suporta: soma, subtração, multiplicação, divisão, potência, raiz quadrada e resto da divisão.
"""

import math


def somar(a: float, b: float) -> float:
    return a + b


def subtrair(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def potencia(a: float, b: float) -> float:
    return a ** b


def raiz_quadrada(a: float) -> float:
    if a < 0:
        raise ValueError("Não existe raiz quadrada de número negativo nos reais.")
    return math.sqrt(a)


def resto_divisao(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a % b


def divisao_inteira(a: float, b: float) -> int:
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a // b


def menu():
    print("\n" + "=" * 40)
    print("         CALCULADORA SIMPLES")
    print("=" * 40)
    print("  1 - Soma (+)")
    print("  2 - Subtração (-)")
    print("  3 - Multiplicação (*)")
    print("  4 - Divisão (/)")
    print("  5 - Potência (x^y)")
    print("  6 - Raiz quadrada (√)")
    print("  7 - Resto da divisão (%)")
    print("  8 - Divisão inteira (//)")
    print("  0 - Sair")
    print("=" * 40)


def ler_numero(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Digite um número válido.")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Até logo!")
            break

        try:
            if opcao == "1":
                a = ler_numero("Primeiro número: ")
                b = ler_numero("Segundo número: ")
                print(f"Resultado: {a} + {b} = {somar(a, b)}")

            elif opcao == "2":
                a = ler_numero("Primeiro número: ")
                b = ler_numero("Segundo número: ")
                print(f"Resultado: {a} - {b} = {subtrair(a, b)}")

            elif opcao == "3":
                a = ler_numero("Primeiro número: ")
                b = ler_numero("Segundo número: ")
                print(f"Resultado: {a} * {b} = {multiplicar(a, b)}")

            elif opcao == "4":
                a = ler_numero("Dividendo: ")
                b = ler_numero("Divisor: ")
                print(f"Resultado: {a} / {b} = {dividir(a, b)}")

            elif opcao == "5":
                a = ler_numero("Base: ")
                b = ler_numero("Expoente: ")
                print(f"Resultado: {a}^{b} = {potencia(a, b)}")

            elif opcao == "6":
                a = ler_numero("Número: ")
                print(f"Resultado: √{a} = {raiz_quadrada(a)}")

            elif opcao == "7":
                a = ler_numero("Dividendo: ")
                b = ler_numero("Divisor: ")
                print(f"Resultado: {a} % {b} = {resto_divisao(a, b)}")

            elif opcao == "8":
                a = ler_numero("Dividendo: ")
                b = ler_numero("Divisor: ")
                print(f"Resultado: {a} // {b} = {divisao_inteira(a, b)}")

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError as e:
            print(f"Erro: {e}")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()
