#!/usr/bin/python
# -*- coding: utf-8 -*-
# Gerador de Passwords Seguras
# Data: 17/07/2017
# Desenvolvedor: Rúben Silva

# Imports

import sys
import random
from random import randint

###########

# Classe Numeros
def numeros():
	# Array com todos os numeros básicos
	numeros = ['1', '2',  '3', '4', '5', '6', '7', '8', '9',]
	# Obtém dois números aleatórios
	randomNumero0 = random.choice(numeros)
	randomNumero1 = random.choice(numeros)
	# Retorna esses numeros
	return randomNumero0
	return randomNumero1

# Classe Letras
def letras():
	# Array com letras comuns a vários teclados
	letras = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
	# Obtém duas letras aletórias
	randomLetra0 = random.choice(letras)
	randomLetra1 = random.choice(letras)
	# Retorna essas letras
	return randomLetra0
	return randomLetra1

# Classe Símbolos
def simbolos():
	# Array com vários simbolos presentes no teclado
	simbolos = ['|', '!', '#', '%', '&', '/', '(', ')', '=', '?', '«', '»', '@', '§', '{', '[', ']', '}', '<', '>', ',', '.', ';', ':', '-', '_', '^', '~', '+', '*', '¨']
	# Obtém dois simbolos aleatórios
	randomSimbolo0 = random.choice(simbolos)
	randomSimbolo1 = random.choice(simbolos)
	# Retorna esses simbolos
	return randomSimbolo0
	return randomSimbolo1

# Classe Password
def password(randomSimbolo0, randomLetra0, randomNumero0, randomSimbolo1, randomLetra1, randomNumero1):
	pass1 = randomSimbolo0 + randomNumero0 + randomLetra0 + randomNumero1 + randomLetra1 + randomSimbolo1 # Estrutura Password
	pass2 = pass1 # Pass 2 igual a pass1 (2 vezes a mesma para que não seja facil de pensa numa repetição)
	password1 = pass1 + pass2
	return password1 # Retorna a Password

# Classe ajuda
def ajuda():
	return """
	COMO USAR: python passGenerate.py
	"""
###########

# Verifica se o argumento 1 é o pedido de ajuda, e em caso afirmativo retorna a mensagem de ajuda
if len(sys.argv) > 1:
	if sys.argv[1] == '-h':
		print (ajuda())
		sys.exit(0)
##########
# Mensagem de Entrada
print ("""
+-----------------------------------------------------+
|                    Pass Generate                    |
+-----------------------------------------------------+
                      Rúben Silva 
""")

# Declaração das respetivas variáveis
randomSimbolo0 = numeros()
randomLetra0 = letras()
randomNumero0 = simbolos()
randomSimbolo1 = numeros()
randomLetra1 = letras()
randomNumero1 = simbolos()

password1 = password(randomSimbolo0, randomLetra0, randomNumero0, randomLetra1, randomSimbolo1, randomNumero1)

print ("A sua Password: " + password1) 
