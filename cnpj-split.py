import os

# Caminho do arquivo de entrada
caminho_arquivo_entrada = 'CNPJ-FORMATADOS.txt'

# Diretório de saída para os novos arquivos (mesma pasta do programa)
diretorio_saida = os.path.dirname(os.path.abspath(__file__))

# Nome base para os novos arquivos
nome_base_arquivo_saida = 'CNPJFORMATADOS_'

# Número de linhas por arquivo
linhas_por_arquivo = 500

# Criar o diretório de saída se não existir
if not os.path.exists(diretorio_saida):
    os.makedirs(diretorio_saida)

# Contador para nomear os novos arquivos
contador_arquivos = 1

# Inicializar listas para armazenar as linhas
linhas = []

# Ler o arquivo de entrada e dividir em arquivos menores
with open(caminho_arquivo_entrada, 'r') as arquivo_entrada:
    for i, linha in enumerate(arquivo_entrada, start=1):
        linhas.append(linha)

        # Se atingir o número máximo de linhas, criar um novo arquivo
        if i % linhas_por_arquivo == 0:
            caminho_arquivo_saida = os.path.join(diretorio_saida, f'{nome_base_arquivo_saida}{contador_arquivos}.txt')
            with open(caminho_arquivo_saida, 'w') as arquivo_saida:
                arquivo_saida.writelines(linhas)
            linhas = []
            contador_arquivos += 1

# Lidar com o restante das linhas que não foram escritas
if linhas:
    caminho_arquivo_saida = os.path.join(diretorio_saida, f'{nome_base_arquivo_saida}{contador_arquivos}.txt')
    with open(caminho_arquivo_saida, 'w') as arquivo_saida:
        arquivo_saida.writelines(linhas)

print(f'Arquivos divididos com sucesso no diretório: {diretorio_saida}')
