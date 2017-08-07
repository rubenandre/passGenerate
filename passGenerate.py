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

def numeros():
	numeros = ['1', '2',  '3', '4', '5', '6', '7', '8', '9',]
	randomNumero0 = random.choice(numeros)
	randomNumero1 = random.choice(numeros)
	return randomNumero0
	return randomNumero1

def letras():
	letras = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
	randomLetra0 = random.choice(letras)
	randomLetra1 = random.choice(letras)
	return randomLetra0
	return randomLetra1

def simbolos():
	simbolos = ['|', '!', '#', '%', '&', '/', '(', ')', '=', '?', '«', '»', '@', '§', '{', '[', ']', '}', '<', '>', ',', '.', ';', ':', '-', '_', '^', '~', '+', '*', '¨']
	randomSimbolo0 = random.choice(simbolos)
	randomSimbolo1 = random.choice(simbolos)
	return randomSimbolo0
	return randomSimbolo1

def password(randomSimbolo0, randomLetra0, randomNumero0, randomSimbolo1, randomLetra1, randomNumero1):
	pass1 = randomSimbolo0 + randomNumero0 + randomLetra0 + randomNumero1 + randomLetra1 + randomSimbolo1
	pass2 = pass1
	password1 = pass1 + pass2
	return password1

def ajuda():
	return """
	COMO USAR: python passGenerate.py
	"""
###########

if len(sys.argv) > 1:
	if sys.argv[1] == '-h':
		print (ajuda())
		sys.exit(0)

print ("""
+-----------------------------------------------------+
|                    Pass Generate                    |
+-----------------------------------------------------+
                      Rúben Silva 
""")

#Definições
randomSimbolo0 = numeros()
randomLetra0 = letras()
randomNumero0 = simbolos()
randomSimbolo1 = numeros()
randomLetra1 = letras()
randomNumero1 = simbolos()

password1 = password(randomSimbolo0, randomLetra0, randomNumero0, randomLetra1, randomSimbolo1, randomNumero1)

print ("A sua Password: " + password1)