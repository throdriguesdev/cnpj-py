# Automatizando Consultas e Registros de CNPJ com Python 🐍

## Sobre o Projeto

Este projeto visa automatizar a consulta e o registro de informações de CNPJ (Cadastro Nacional da Pessoa Jurídica) utilizando a linguagem Python. É uma ferramenta eficiente e organizada que consome a API disponibilizada pela Receita Federal.

## Principais Recursos

- **Consulta e Registro de CNPJ:** Insira CNPJs para consulta, e o sistema consumirá a API da Receita Federal para obter os dados de retorno.

- **Armazenamento Inteligente:** Utilizamos a biblioteca `pandas` para armazenar os dados de forma organizada em uma planilha Excel. Se a planilha não existir, o programa a cria automaticamente.

- **Controle de Taxa de Consulta:** O projeto respeita o limite de consultas por minuto imposto pela API gratuita da Receita Federal, evitando erros de requisição.

- **Gerenciamento de Erros:** Implementamos tratamento de erros e geração de relatórios para detalhar possíveis falhas. O relatório é ativado no término do programa, com ou sem erros.

## Tecnologias Utilizadas

- **Python:** A linguagem principal do projeto.

- **Bibliotecas Python:** Utilizamos `pandas` para organização de dados, `requests` para solicitações HTTP, `tqdm` para barras de progresso e `logging` para gerenciamento de logs.

## Como Utilizar

1. Clone o repositório para sua máquina local.
2. Instale as bibliotecas necessárias com `pip install -r requirements.txt`.
3. Execute o programa e insira os CNPJs desejados para consulta.

## Contribuições

Sinta-se à vontade para contribuir, sugerir melhorias ou usar o projeto para suas próprias necessidades. Basta fazer um fork do repositório, criar um branch para suas modificações e enviar um pull request.



