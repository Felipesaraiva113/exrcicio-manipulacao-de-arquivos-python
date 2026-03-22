import os 
print(os.getcwd())
lista_arquivos = os.listdir('arquivos')
print(lista_arquivos)
for nome_arquivo in lista_arquivos:
    if 'html' in nome_arquivo:
        if '2' in nome_arquivo:
            os.rename(f'arquivos/{nome_arquivo}', f'arquivos2/{nome_arquivo}')
        elif '1' in nome_arquivo:
            os.rename(f'arquivos/{nome_arquivo}', f'arquivos3/{nome_arquivo}')
            