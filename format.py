import os

# Caminho do diretório atual
diretorio_atual = r'C:\Users\thiago.rodrigues\cnpj-py'

# Caminho do arquivo de entrada (linhas_com_cnpj.txt)
caminho_arquivo_entrada = os.path.join(diretorio_atual, 'linhas_com_cnpj.txt')

# Caminho do arquivo de saída para linhas com CNPJ formatados
caminho_arquivo_saida_com_cnpj = os.path.join(diretorio_atual, 'linhas_com_cnpj_formatados.txt')

# Lendo o arquivo linhas_com_cnpj.txt
with open(caminho_arquivo_entrada, 'r') as arquivo_entrada:
    # Abrir o arquivo de saída para escrita
    with open(caminho_arquivo_saida_com_cnpj, 'w') as arquivo_saida:
        # Iterar sobre cada linha do arquivo de entrada
        for linha in arquivo_entrada:
            # Remover espaços em branco do início e do final da linha
            linha = linha.strip()

            # Verificar se a linha não está vazia
            if linha:
                # Remover pontos, barras e traço do CNPJ e escrever no arquivo de saída
                cnpj_formatado = linha.replace('.', '').replace('/', '').replace('-', '')
                arquivo_saida.write(cnpj_formatado + '\n')

print("CNPJs formatados foram salvos em", caminho_arquivo_saida_com_cnpj)
