# ADEMIR GUIMARÃES DA COSTA JUNIOR

def func(x, y):
    return eval(EDO)


def RK4(xi, yi, x, h):
    """
    :param xi: Valor inicial de X
    :param yi: Valor inicial de Y
    :param x: Valor final de X
    :param h: Passo de crescimento
    :return: Valor final de Y
    """

    n = round(((x - xi) / h))  # A quantidade de vezes que o passo deve ser aplicado

    for i in range(n):
        k1 = func(xi, yi)
        k2 = func(xi + 0.5 * h, yi + 0.5 * h * k1)
        k3 = func(xi + 0.5 * h, yi + 0.5 * h * k2)
        k4 = func(xi + h, yi + h * k3)

        # SUBSTITUINDO VALOR DE Y E X

        yi = yi + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        xi = xi + h

    return yi


if __name__ == '__main__':
    print("Feito por: Ademir Guimarães")
    # Aplicando o PVI
    loop = True
    while loop:
        EDO = input("Digite sua função: ")
        print("-------PVI-------")
        x0 = float(input("Qual o valor inicial de X? "))  # VALOR INICIAL DE X
        y0 = float(input(f"Qual o de inicial de Y? "))
        xf = float(input("Qual o valor final de x? "))
        h_ = float(input("Qual o passo? "))  # PASSO
        print(f'\nO valor de y({xf}) = {RK4(x0, y0, xf, h_)}')

        resp = input("Você deseja continuar? Digite 'S' para sim e 'N' para não.\n")
        if resp == 'N' or resp == 'n':
            loop = False
        elif resp == 'S' or resp == 's':
            pass
        else:
            resp = input("Você deseja continuar? Digite 'S' para sim e 'N' para não.")
