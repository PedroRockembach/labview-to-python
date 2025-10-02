import os
import openpyxl

texto_exemplo = 'Teste15_C1_Pressao_TCH25630013-C1-FOLGA-0,85mm-Cavidade-5-TesteDia29.txt'

def _txtToExel(exemplo):
    lista_passagem = []
    
    with open(exemplo,"r") as ex:
        for i in ex:
            lista_passagem.append(i)
            
            if lista_passagem[i] == '\n':
                print('\n')
            else:    
                print(lista_passagem)
        
if __name__ == "__main__":
    _txtToExel(texto_exemplo)