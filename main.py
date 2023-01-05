n1 = input('Digite um número: ') #Pega o dado do usuario

try:                               #Tenta executar essa condição, caso seja verdadeira ela é executada.
    n1_convertido = int(n1)      #Converte o dado recebido para um número inteiro
    if n1_convertido % 2 == 0:   #Verifica se o resto da divisão desse número por 2 é igual a 0
        print(f'O numero {n1_convertido} é par')
    else:                        #Se o resto da divisão nao for 0 o número é impar
        print('O número é impar')

except:                          #Caso a condição a cima seja falsa, o except é executado.
    print('Voce nao digitou um número')

