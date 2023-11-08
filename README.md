# CNPJ - pyth

Aplicativo que consome API da receita federal para automatizar buscas por CNPJ, e retornar dados de interesse em uma planilha.
Programa permite armazenar diversos CNPJ para realizar a consulta, respeitando o tempo limite da api (3 por miniuto).

## Pré-requisitos

Antes de começar, certifique-se de ter instalado os seguintes requisitos:

- Python 
- Bibliotecas Python: pandas, requests, tqdm

## Instalação

1. Clone o repositório:

  
   git clone https://github.com/throdriguesdev/cnpj-py/
pip install pandas requests tqdm
Adicione os CNPJs que você deseja consultar à lista cnpjs no código.

Execute o script Python:
python nome-do-seu-script.py
O script irá consultar os CNPJs listados e salvar os dados em um arquivo Excel chamado dados_cnpj.xlsx.

Contribuição
Fork o projeto.
Crie uma nova branch com a sua feature: git checkout -b feature-nova.
Commit suas mudanças: git commit -m 'Adicione alguma feature'.
Push para a branch: git push origin feature-nova.
Envie um Pull Request.
