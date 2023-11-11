import os
import pandas as pd

# Obtendo o caminho do diretório atual onde o script está sendo executado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Lendo a planilha
try:
    planilha = pd.read_excel('BASECNPJ.xlsx')
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
    # Lidar com a situação de arquivo ausente

# Verificando se a coluna 'CNPJ' existe
if 'CNPJ' not in planilha.columns:
    print("A coluna 'CNPJ' não existe na planilha.")
    # Lidar com a situação de coluna ausente

# Filtrando linhas com CNPJ não vazio
linhas_com_cnpj = planilha.dropna(subset=['CNPJ'])

# Filtrando linhas com CNPJ vazio
linhas_sem_cnpj = planilha[planilha['CNPJ'].isnull()]

# Salvando linhas com CNPJ em um arquivo TXT na mesma pasta que o script
linhas_com_cnpj[['CNPJ']].to_csv(os.path.join(diretorio_atual, 'linhas_com_cnpj.txt'), index=False, header=True, sep='\t')

# Salvando 'Conta Cliente' das linhas sem CNPJ em outro arquivo TXT na mesma pasta que o script
linhas_sem_cnpj[['Conta Cliente']].to_csv(os.path.join(diretorio_atual, 'linhas_sem_cnpj.txt'), index=False, header=True, sep='\t')
