from math import  *
#Nombre: Roberto Hernandez
#Cedula: 28074932

'''Funcion'''
def f(x):
    return sqrt(x+1)

'''Suma de riemann'''
def suma_riemann(f,a,b,n):
	h = (b-a)/n
	acum = 0
	for i in range (n):
		x=a+i*h
		acum = acum+h*f(x)
	return acum

if __name__ == '__main__':
    a = -1      # inicio del intervalo
    b = 1     # fin del intervalo
    n = 5   # numero de participaciones

    riemann = suma_riemann(f, a, b, n)

    print("\t.:Metodo del Riemann:.")
    print("-------------------------------------")
    print("Suma de Riemann en funcion f(x) para",a," y ",b, "en ", n, " intentos: ",riemann)
    print("-------------------------------------")
