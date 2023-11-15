#estrategia 02

lista = [10,2,5,7,6,3]

soma=0
for num in lista:
    if(num%2==0):
        soma=soma+num
print('O somatório dos elementos pares da lista é: {}'.format(soma))