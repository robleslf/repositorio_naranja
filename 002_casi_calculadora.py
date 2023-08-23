import random

def calculate_approximate_sum(num1, num2, min_error, max_error):
    sum_result = num1 + num2
    error = random.uniform(min_error, max_error)
    return sum_result + error

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

min_error = -1   # Rango de error mínimo
max_error = 2    # Rango de error máximo

result = calculate_approximate_sum(num1, num2, min_error, max_error)
print(f"Más o menos la suma es {result:.2f} o algo así")
