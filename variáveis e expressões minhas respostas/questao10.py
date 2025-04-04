"""Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s ˆ
(metros por segundo). A formula de conversao˜ e: ´ M = K/3.6, sendo K a velocidade em
km/h e M em m/s.
"""
km = float(input("Digite sua velocidade em Km aqui: "))
converMETROS = (km/3.6)
print(f"A velocidade em metros por segundo é {converMETROS:.2f}")
