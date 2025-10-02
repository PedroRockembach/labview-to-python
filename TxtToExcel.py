import os
import openpyxl

texto_exemplo = 'Teste15_C1_Pressao_TCH25630013-C1-FOLGA-0,85mm-Cavidade-5-TesteDia29.txt'

def _txtToExel(txt_pressao):
    lines = []
    
    with open(txt_pressao,"r") as ex:
        for line in ex:
            if line.strip():
                columns = line.strip().split('\t')
                lines.append(columns)
        return lines
            
        
        
if __name__ == "__main__":
    _txtToExel(texto_exemplo)