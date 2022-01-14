'''
Ley de la suma

'''
def f(n):
    for i in range (m):
        print(i)

    for i in range (n):
        print (i)

'''
Tenemos  dos loops que dependen de n. En ambos nos tarnamos n pasos.

Podemos decir que tenemos Big o Notacion de n:
 
 O(n) + O(n) = O(n + n) = O(2n)

 Lo que impora no son los terminos especificos, sino como se comporta la funcion
 Nuestra funcion crece de manera lineal, es decir, si nuestro n es 2 va tardar el doble yasi susesivamente.

Es una funcion  crece en Big O of n

O(n)
'''

def f(n):
    for i in range (m):
        print(i)

    for i in range (n*n):
        print (i)

'''
O(n) + O(n*n) = O(n + n^2)

En Big O nos importa el termino mas grnde

 O(n^2)

 Es una funcion  crece en Big O of n^2
'''

def f(n):
    for i in range (n):
        for j in range (n):
        print (i,j)

'''       
 O(n) * O(n) = O(n * n) = O(n^2)

En Big O nos importa el termino mas grnde

 O(n^2)

 Es una funcion  crece en Big O of n^2
'''