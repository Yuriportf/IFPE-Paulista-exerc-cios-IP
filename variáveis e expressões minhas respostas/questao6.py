"""Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A formula de conversao e: F = C∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius."""
grauscelsius = float(input("Digite os seus Graus Celsius aqui: "))
formulafahrenheit = (grauscelsius * 5 / 9) + 32
print(formulafahrenheit)