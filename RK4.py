# ADEMIR GUIMARÃES DA COSTA JUNIOR

import math

def func(x, y, edo):
    """
    Avalia a expressão da EDO fornecida, substituindo x e y nas variáveis da equação.
    :param x: Valor de X.
    :param y: Valor de Y.
    :param edo: Expressão da EDO como string.
    :return: Resultado da função EDO avaliada.
    """
    try:
        # Permitir funções matemáticas e as variáveis x, y
        return eval(edo, {"__builtins__": None}, {'x': x, 'y': y, **math.__dict__})
    except NameError as e:
        raise ValueError("Erro na avaliação da EDO: verifique a fórmula inserida.") from e


def runge_kutta_4(xi, yi, xf, h, edo):
    """
    Método de Runge-Kutta de 4ª ordem para resolver EDOs.
    :param xi: Valor inicial de X.
    :param yi: Valor inicial de Y.
    :param xf: Valor final de X.
    :param h: Passo.
    :param edo: Expressão da EDO como string.
    :return: Valor final de Y.
    """
    n = int((xf - xi) / h)

    for _ in range(n):
        k1 = func(xi, yi, edo)
        k2 = func(xi + h / 2, yi + h / 2 * k1, edo)
        k3 = func(xi + h / 2, yi + h / 2 * k2, edo)
        k4 = func(xi + h, yi + h * k3, edo)

        yi += (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        xi += h

    return yi


def obter_parametros():
    """
    Solicita os parâmetros de entrada ao usuário.
    :return: Tupla com os valores de x0, y0, xf, h e a EDO.
    """
    try:
        edo = input("Digite a equação diferencial (use 'x' e 'y'): ").strip()
        x0 = float(input("Digite o valor inicial de X: "))
        y0 = float(input("Digite o valor inicial de Y: "))
        xf = float(input("Digite o valor final de X: "))
        h = float(input("Digite o passo: "))
        return x0, y0, xf, h, edo
    except ValueError:
        print("Erro: valor numérico inválido.")
        return obter_parametros()  # Reinicia a entrada se houver erro


def main():
    print("Feito por: Ademir Guimarães")
    
    while True:
        x0, y0, xf, h, edo = obter_parametros()
        
        try:
            resultado = runge_kutta_4(x0, y0, xf, h, edo)
            print(f"\nO valor de y({xf}) = {resultado}")
        except ValueError as e:
            print(e)

        # Pergunta se deseja continuar
        continuar = input("Deseja realizar outro cálculo? (S/N): ").strip().lower()
        if continuar != 's':
            print("Encerrando o programa.")
            break


if __name__ == '__main__':
    main()

