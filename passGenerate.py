#!/usr/bin/python
# -*- coding: utf-8 -*-

# Gerador de Passwords Seguras
# Data Inicio Projeto: 17/07/2017
# Data Última Correção: 05/01/2018
# Desenvolvedor: Rúben Silva

# Imports necessários ao projeto

import sys
import random
from random import randint

###########

# Classe responsável por gerar números aleatórios
def numeros():
	# Array com todos os numeros básicos
	numeros = ['1', '2',  '3', '4', '5', '6', '7', '8', '9', '0']
	# Obtém números aleatórios
	randomNumero = random.choice(numeros)
	# Retorna esses numeros
	return randomNumero

# Classe responsável por gerar letras aleatórias
def letras():
	# Array com letras comuns a vários teclados
	letras = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
	# Obtém letras aletórias
	randomLetra = random.choice(letras)
	# Retorna essas letras
	return randomLetra

# Classe responsável por gerar símbolos aleatórios (os mais usais)
def simbolos():
	# Array com vários simbolos presentes no teclado
	simbolos = ['!', '#', '%', '&', '/', '(', ')', '=', '?', '«', '»', '@', '{', '[', ']', '}', '<', '>', ':', '-', '_', '+', '*']
	# Obtém simbolos aleatórios
	randomSimbolo = random.choice(simbolos)
	# Retorna esses simbolos
	return randomSimbolo

# Classe que gera a password
def password(randomLetra0, randomNumero0, randomLetra1, randomLetra2, randomNumero1, randomSimbolo, randomNumero2, randomLetra3, randomNumero3, randomLetra4):
	# pass1 = primeira estrutura da password
	pass1 = randomLetra0 + randomNumero0 + randomLetra1 + randomLetra2 + randomNumero1
	# pass2 = segunda estrutura da password
	pass2 = randomSimbolo + randomNumero2 + randomLetra3 + randomNumero3 + randomLetra4
	# Uniao de ambas as estruturas
	password1 = pass1 + pass2
	# Retorna a Password
	return password1

# Classe que mostra a mensagem de ajuda
def ajuda():
	return """
	COMO USAR: python passGenerate.py
	"""

# Verifica se o argumento 1 é o pedido de ajuda, e em caso afirmativo retorna a mensagem de ajuda
if len(sys.argv) > 1:
	if sys.argv[1] == '-h':
		print (ajuda())
		sys.exit(0)

# Mensagem de Entrada a cada execução
print ("""
+-----------------------------------------------------+
|                    Pass Generate                    |
+-----------------------------------------------------+
                      Rúben Silva
""")

# Declaração das respetivas variáveis
# Cada variavel, aceda a uma respetiva classe, onde é gerado o respetivo pedido
randomLetra0 = letras()
randomNumero0 = numeros()
randomLetra1 = letras()
randomLetra2 = letras()
randomNumero1 = numeros()
randomSimbolo = simbolos()
randomNumero2 = numeros()
randomLetra3 = letras()
randomNumero3 = numeros()
randomLetra4 = letras()

# Processo que acessa a classe password para gerar uma password
password1 = password(randomLetra0, randomNumero0, randomLetra1, randomLetra2, randomNumero1, randomSimbolo, randomNumero2, randomLetra3, randomNumero3, randomLetra4)

print ("A sua Password: " + password1)
