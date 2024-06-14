import numpy as np

# Palavra para calcular o produto das matrizes
matriz_codificadora = np.array(
    [
        [ord('F'), ord('A')],
        [ord('C'), ord('A')],
    ]
)

# Frase
frase = "ROMA NAO FOI CONSTRUIDA EM UM DIA"

def codificar(frase, palavra):
    frase_codificada = ''
    # Verificando se o comprimento da frase é par
    if len(frase) % 2 != 0:
        frase += "X"  # Adicionando 'X' para tornar o comprimento par

    # Dividindo a frase em pares de letras
    for i in range(0, len(frase), 2):
        par = frase[i:i+2]

        # Convertendo cada par em uma matriz
        matriz = np.array([[ord(par[0])], [ord(par[1])]])

        # Calculando o produto da matriz codificadora com a matriz do par de letras
        calculo = np.dot(palavra, matriz)

        # Calculando o módulo de 127 para manter os caracteres na tabela ASCII
        # e convertendo o resultado de volta para caracteres
        for i, num in enumerate(calculo):
            if num > 127:
                resultado = num % 127
                frase_codificada += chr(resultado[0])
            else:
                num = num % 127
                frase_codificada += chr(resultado[0])

    return frase_codificada
        
def decodificar(frase_codificada, palavra):
    frase_decodificada = ''

    determinante_palavra = np.linalg.det(palavra)

    inversa = np.linalg.inv(palavra)

    inversa = np.round(determinante_palavra * inversa).astype(int)

    # Ajustando valores da matriz inversa para estarem no intervalo de caracteres ASCII
    for i in range(len(inversa)):
        for j in range(len(inversa[i])):
            if inversa[i][j] > 127 or inversa[i][j] < 0:
                inversa[i][j] = inversa[i][j] % 127

    determinante = np.linalg.det(palavra)

    # Encontrando o inverso multiplicador modular
    for i in range(1, 127):
        if ((i * int(determinante)) % 127) == 1:
            inverso_multiplicador = i
            break

    matriz_decodificadora = np.dot(inverso_multiplicador, inversa)

    # Ajustando valores da matriz decodificadora
    for i in range(len(matriz_decodificadora)):
        for j in range(len(matriz_decodificadora[i])):
            if matriz_decodificadora[i][j] > 127 or matriz_decodificadora[i][j] < 0:
                matriz_decodificadora[i][j] = matriz_decodificadora[i][j] % 127
    
    # Decodificando cada par de caracteres codificados
    for i in range(0, len(frase_codificada), 2):
        par = frase_codificada[i:i+2]

        matriz = np.array([[ord(par[0])], [ord(par[1])]])

        calculo = np.dot(matriz_decodificadora, matriz)

        for i, num in enumerate(calculo):
            if num > 127:
                resultado = num % 127
                frase_decodificada += chr(int(resultado[0]))
            else:
                num = num % 127
    
    print(frase_decodificada)

palavra_codificada = codificar(frase, matriz_codificadora)

decodificar(palavra_codificada, matriz_codificadora)
