print("ADVERTENCIA: Por favor, asegúrate de ingresar números válidos. Los valores negativos o cero pueden causar errores o resultados inesperados.")
# importa librería math
import math
# Solicitud de Inputs
P_Supcripcion = float(input("Ingrese el precio de suscripción en [$]:\n>"))
N_UsuariosN = float(input("Ingrese el número de usuarios normales:\n>"))
N_UsuariosP = float(input("Ingrese el número de usuarios premiuns:\n>"))
G_Totales = float(input("Ingrese los gastos totales en [$]:\n>"))
# Formula
C_UsarioNormal=(P_Supcripcion*N_UsuariosN)
C_UsarioPremiun=(1.5*P_Supcripcion*N_UsuariosP)
Utilidades = (C_UsarioNormal+C_UsarioPremiun)-G_Totales
# Entrega el resultado aproximado al entero siguiente
print(f'Las utilidades de: {math.ceil(Utilidades)} [$]')
