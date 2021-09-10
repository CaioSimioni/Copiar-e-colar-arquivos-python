import os
import shutil

"""
[pt-br]
autor: Caio Ribeiro Simioni

-Referências:
Como mover, copiar e apagar arquivos com Python - Aula 32 = https://www.youtube.com/watch?v=m8orGLxO03s

<código referência>{

    for root, dirs, files in os.walk(caminho+r'\PastaTesteOrigem'):
        for file in files:
            path_origem = os.path.join(root, file)
            path_destino = os.path.join(caminho+r'\PastaTesteDestino', file)
            if '.txt' in file:
                os.remove(path_destino)
                shutil.copy(path_origem, path_destino)
                print('OK!')

}

-Objetivo:
Conseguir mover arquivos, substituindo-os através da referência do caminho das pastas.

"""
print('')
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
