#open recebe o caminho e como sera abertp

#r de leitura
#open("caminho", "r")

#a append incrementar

# w esscrita

#x criar arquivo

#r+ leitura mais escrita


#sempre que abrir um aquivo feche ele
#arquivo = open('dataManipulation/teste.txt',"a")

#cria um arquivo
arquivo = open('dataManipulation/teste2.txt',"x")

            #LEITURA
#verifica se o arquivo pode ser lido 
#print(arquivo.readable())

#le o arquivo
#print(arquivo.read())

#le a primeira linha
#print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())

#transforma os item==ns denro do arquivo em uma lista
#lista =  arquivo.readlines()
#print(lista[4])



                                #ESCRITA
#adicona coisas em um arquivo ja existente no lugar do primeiro item
arquivo.write("\nC++")


                #EXCLUI

#importar biblioteca que nao estao ativa

import os

arquivo.close()

#checa se o arquivo existe 
#os.path.exists('dataManipulation/teste2.txt')

#os.remove('dataManipulation/teste2.txt')

#remove pasta somente se a mesma estivez vazia
os.rmdir('dataManipulation/nova_pasta')