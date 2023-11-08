import requests
import pandas as pd
import time
from tqdm import tqdm
import logging

# inicializar DataFrame
df = pd.DataFrame()
arquivo_progresso = "progresso.txt"
consultas_por_minuto = 3
tempo_espera = 60 / consultas_por_minuto

# lista de CNPJs separados por vírgula (máximo de 1000 CNPJs)
cnpjs = [
    "00191498001350",
    "17660814000155",
    "27826790000115",
    # adicionar mais CNPJs aqui, até um máximo de 1000
]

# configuração da barra de progresso personalizada
total_cnpjs = len(cnpjs)
bar_format = '{l_bar}{bar}| [{elapsed}<{remaining}] {n_fmt}/{total_fmt} {rate_fmt}'
barra_progresso = tqdm(total=total_cnpjs, unit="CNPJ", ncols=100, bar_format=bar_format)

# função para buscar campos
def buscar_campos(cnpj):
    try:
        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return {
                "Nome": data.get("nome"),
                "Fantasia": data.get("fantasia"),
                "CNPJ": cnpj,
                "Status": data.get("status"),
                "Tipo": data.get("tipo"),
                "Atividade Principal - Código": data.get("atividade_principal")[0].get("code") if data.get("atividade_principal") else "N/A",
                "Atividade Secundária - Código": data.get("atividades_secundarias")[0].get("code") if data.get("atividades_secundarias") else "N/A",
                "Atividade Principal - Texto": data.get("atividade_principal")[0].get("text") if data.get("atividade_principal") else "N/A",
                "Atividade Secundária - Texto": data.get("atividades_secundarias")[0].get("text") if data.get("atividades_secundarias") else "N/A",
                "Natureza Jurídica": data.get("natureza_juridica"),
                "Logradouro": data.get("logradouro"),
                "Número": data.get("numero"),
                "CEP": data.get("cep"),
                "Bairro": data.get("bairro"),
                "Município": data.get("municipio"),
                "UF": data.get("uf"),
                "Telefone": data.get("telefone"),
                "Email": data.get("email"),
                "Situação": data.get("situacao"),
                "Capital Social": data.get("capital_social"),
                "Última Atualização": data.get("ultima_atualizacao"),
            }
        else:
            if response.status_code == 429:
                mensagem = f"Erro ao consultar o CNPJ {cnpj}: Muitas solicitações. Aguarde para continuar."
            else:
                mensagem = f"Falha na consulta do CNPJ {cnpj}. Código de Status: {response.status_code}"
            logging.error(mensagem)
            print(mensagem)  # Mensagem de erro
    except Exception as e:
        mensagem = f"Erro ao consultar o CNPJ {cnpj}: {str(e)}"
        logging.error(mensagem)
        print(mensagem)  # Mensagem de erro

    return {}  # Retorna um dicionário vazio se a consulta falhar

# função para formatar a mensagem de progresso
def formatar_mensagem_progresso(cnpj):
    return f"Consultando CNPJ {cnpj}..."

# itera sobre a lista de CNPJs
for cnpj in cnpjs:
    try:
        mensagem_progresso = formatar_mensagem_progresso(cnpj)
        print(mensagem_progresso, end=" ", flush=True)
        
        cnpj_data = buscar_campos(cnpj)

        if not cnpj_data:
            logging.warning(f"Falha ao obter dados para CNPJ {cnpj}. Pulando esta iteração.")
            print("Pulado.")  # mensagem de progresso
            continue  # pule esta iteração se a consulta falhar

        # DataFrame com os novos dados
        new_df = pd.DataFrame([cnpj_data])
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_excel("dados_cnpj.xlsx", index=False)
        barra_progresso.update(1)
        print("Salvo.")  # Mensagem de progresso
        # taxa de consultas
        time.sleep(tempo_espera)
    except Exception as e:
        logging.error(f"Erro inesperado ao processar o CNPJ {cnpj}: {str(e)}")
barra_progresso.close()
# dados foram salvos com sucesso
print(f"Dados salvos com sucesso para {len(cnpjs)} CNPJs.")
