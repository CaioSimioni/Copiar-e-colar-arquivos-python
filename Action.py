import os
import shutil

"""
[pt-br]
autor: Caio Ribeiro Simioni

-Referências:
Como mover, copiar e apagar arquivos com Python - Aula 32 = https://www.youtube.com/watch?v=m8orGLxO03s

-Objetivo:
Conseguir mover arquivos, substituindo-os através da referência do caminho das pastas.

"""

caminhoOrigem  = r'<caminho das pastas>'  # Arquivo que será copiado
caminhoDestino = r'<caminho das pastas>' # Arquivo que será substituído

try:
    os.remove(caminhoDestino+r'\ABC.txt')
    shutil.copy(caminhoOrigem+r'\ABC.txt', caminhoDestino+r'\ABC.txt')
    print('Funcionou!')
except NameError:
    print('Não funcionou!')
    raise

os.system('PAUSE')
