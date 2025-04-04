"""Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
formula de conversao e:´ C = K − 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
"""
Graukelvin = float(input("Digite a sua temperatura em Gráus Kelvin: "))
convercelsius = (Graukelvin - 273.15)
print(f"a converção de Graus Kelvin para Celsius é {convercelsius}")