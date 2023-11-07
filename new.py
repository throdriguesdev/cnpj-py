import requests

cnpjs = ["09464629000248", "41044009000181", "09464629000167"]

# Itera sobre a lista de CNPJs
for cnpj in cnpjs:
    # URL da API
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"

    # Cabeçalhos necessários
    headers = {"Accept": "application/json"}

    # Solicitação GET para a API
    response = requests.get(url, headers=headers)

    # Verifique se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        data = response.json()

        # Imprima os campos desejados
        print("Status:", data.get("status"))
        print("Última Atualização:", data.get("ultima_atualizacao"))
        print("CNPJ:", data.get("cnpj"))
        print("Tipo:", data.get("tipo"))
        print("Nome:", data.get("nome"))
        
        # Atividade Principal
        atividade_principal = data.get("atividade_principal", [])[0]
        print("Atividade Principal - Texto:", atividade_principal.get("text"))
        print("Atividade Principal - Código:", atividade_principal.get("code"))
        
        # Atividades Secundárias
        atividades_secundarias = data.get("atividades_secundarias", [])
        for atividade in atividades_secundarias:
            print("Atividade Secundária - Texto:", atividade.get("text"))
            print("Atividade Secundária - Código:", atividade.get("code"))
        
        print("Natureza Jurídica:", data.get("natureza_juridica"))
        print("Logradouro:", data.get("logradouro"))
        print("Número:", data.get("numero"))
        print("CEP:", data.get("cep"))
        print("Bairro:", data.get("bairro"))
        print("Município:", data.get("municipio"))
        print("UF:", data.get("uf"))
        print("Telefone:", data.get("telefone"))
        print("Situacao:", data.get("situacao"))
        print("Capital Social:", data.get("capital_social"))
