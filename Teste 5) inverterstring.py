def inverter_string(texto):
    texto_invertido = ""
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

entrada = input("Digite uma string para ser invertida: ")

resultado = inverter_string(entrada)

print(f"String original: {entrada}")
print(f"String invertida: {resultado}")
