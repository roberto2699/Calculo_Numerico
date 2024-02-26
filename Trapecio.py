from math import  *
#Nombre: Roberto Hernandez
#Cedula: 28074932

# Funcion
def f(x):
    return sqrt(x+1)

# Metodo de trapecio
def trapecio(f, a, b, n):
    h = (b - a) / n
    suma = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i*h
        suma += f(x)
    return h * suma

if __name__ == '__main__':
    a = -1      # inicio del intervalo
    b = 1     # fin del intervalo
    n = 5   # numero de participaciones

    trapecio = trapecio(f, a, b, n)

    print("\t.:Integracion Numerica:.")
    print("-------------------------------------")
    print("Metodo de Trapecio en funcion f(x) para",a," y ",b," en ",n,"intentos: ",trapecio)
    print("-------------------------------------")
