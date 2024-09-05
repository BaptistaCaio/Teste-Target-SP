def fibonacci_sequence(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def checar_fibonacci(number):
    sequence = fibonacci_sequence(number)
    if number in sequence:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} não pertence à sequência de Fibonacci."

# Solicitar o número ao usuário no terminal da IDE
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

resultado = checar_fibonacci(numero)
print(resultado)
