import requests
import pandas as pd
import time

# lista de CNPJs separados por vírgula
cnpjs = [
    "00191498001350",
    "17660814000155",
    "27826790000115",
]

# verificar se o arquivo 'dados_cnpj.xlsx' já existe
try:
    df = pd.read_excel("dados_cnpj.xlsx")
except FileNotFoundError:
    # se o arquivo não existir, criar um DataFrame vazio
    df = pd.DataFrame()

# número máximo de consultas por minuto
consultas_por_minuto = 3

# tempo de espera entre consultas (em segundos)
tempo_espera = 60 / consultas_por_minuto

# função para buscar   campos
def buscar_campos(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return {
            "Nome": data.get("nome"),
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
            "Situação": data.get("situacao"),
            "Capital Social": data.get("capital_social"),
            "Última Atualização": data.get("ultima_atualizacao"),
            "FANTASIA": data.get("fantasia")
        }
    return {}  # Retorna um dicionário vazio se a consulta falhar

# Itera sobre a lista de CNPJs
for cnpj in cnpjs:
    cnpj_data = buscar_campos(cnpj)

    if not cnpj_data:
        continue  # Pule esta iteração se a consulta falhar

    # Crie um novo DataFrame com os novos dados
    new_df = pd.DataFrame([cnpj_data])

    # Adicione os novos dados ao DataFrame existente
    df = pd.concat([df, new_df], ignore_index=True)

    # Salve a planilha de volta no mesmo arquivo
    df.to_excel("dados_cnpj.xlsx", index=False)

    # Espere o tempo necessário para respeitar a taxa de consultas
    time.sleep(tempo_espera)
