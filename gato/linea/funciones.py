'''
Archvivo con todas las funciones necesarisas para la aplicación"linea"
'''
import matplotlib.pyplot as plt

def calcular_y(x: float, m:float, b:float)->float:
    '''
        Calcula "y" de acuerdo a la pendiente "m" y el punto de intersección en y "b"
        Retorna el valor de "y"
    '''
    return m*x+b

def grafica_linea(X: list, Y: list, m:float, b:float):
    '''
    Grafica una línea recta
    X: lista de valores de x
    Y: lista de valores de y
    m: pendiente
    b: intersección en y
    '''

    plt.plot(X,Y)
    plt.tittle(f'Línea con pendiente={m} e intersección en y={b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()

#def test_linea():



if __name__ == "__main__":
    x = 0
    m = 3
    b = 2
    y = calcular_y(x,m,b)
    if y==2:
        print("Prueba exitosa")
    else:
        print("Prueba fallida")