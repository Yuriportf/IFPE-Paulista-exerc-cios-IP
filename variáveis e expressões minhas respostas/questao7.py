"""Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A formula de convers ao e: ´ C = 5.0 ∗ (F − 32.0)/9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit."""
Fahrenheit = float(input("Digite os seus graus Fahrenheit aqui: "))
formulacelsius = 5 * (Fahrenheit - 32)/9
print(formulacelsius)