# Boletim de Vulnerabilidades

Este repositório contém um projeto para gerar um boletim de vulnerabilidades utilizando dados obtidos da API NVD (National Vulnerability Database). O projeto permite visualizar as vulnerabilidades de acordo com sua severidade (Crítica, Alta, Média e Baixa), e exibe detalhes dessas vulnerabilidades em um formato HTML responsivo.

## Estrutura do Projeto

- **boletim_cves.py**: Script Python responsável por buscar dados de vulnerabilidades na API NVD, organizar esses dados por severidade, e renderizar um relatório em HTML.
- **templates/**: Diretório que contém o template HTML (`dashboard.html`) usado para renderizar o boletim de vulnerabilidades.
- **Boletim_CVE.html**: Arquivo HTML gerado pelo script, que exibe o boletim com gráficos e detalhes das vulnerabilidades.

## Funcionalidades

1. **Coleta de Dados**: O script coleta dados de vulnerabilidades dos últimos 7 dias usando a API NVD.
2. **Agrupamento por Severidade**: As vulnerabilidades são agrupadas em categorias de severidade: Crítica, Alta, Média e Baixa.
3. **Geração de Gráficos**: Um gráfico de barras é gerado para visualizar o número de vulnerabilidades em cada categoria.
4. **Detalhamento de Vulnerabilidades**: Ao clicar em um botão de severidade no boletim, são exibidos os detalhes das vulnerabilidades daquela categoria.
5. **Responsividade**: O boletim HTML gerado é responsivo, se adaptando a diferentes tamanhos de tela.

## Requisitos

- *Python 3.6 ou superior*
- *Bibliotecas Python*:
  - `nvdlib`: Para buscar dados da API NVD
  - `pandas`: Para manipulação de dados
  - `plotly`: Para geração de gráficos
  - `jinja2`: Para renderização do template HTML

## Como Usar

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/boletim-de-vulnerabilidades.git
   cd boletim-de-vulnerabilidades
   ```
   
2. **Instale as dependências necessárias**:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Configure sua chave da API NVD**:

Edite o arquivo boletim_cves.py e substitua 'SUA_CHAVE_NVD' pela sua chave da API NVD.

   ```bash
   git clone https://github.com/seu-usuario/boletim-de-vulnerabilidades.git
   cd boletim-de-vulnerabilidades
   ```

4. **Execute o script para gerar o boletim**:
   ```bash
   python3 boletim_cves.py
   ```

## Personalização

1. **Alterar o Período de Coleta de Dados**:

O período de coleta de dados pode ser ajustado editando o cálculo de datas no script boletim_cves.py:

   ```bash
   end = datetime.datetime.now()
   start = end - datetime.timedelta(days=7)  # Altere "7" para o número de dias desejado
   ```
   
2. **Clone este repositório**:

As cores das categorias de severidade podem ser ajustadas no arquivo dashboard.html:

   ```bash
.critical { background-color: #800080; }  /* Roxo */
.high { background-color: #FF0000; }      /* Vermelho */
.medium { background-color: #FFA500; }    /* Laranja */
.low { background-color: #FFFF00; color: #000000; }  /* Amarelo com texto preto */
   ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias no código ou na documentação.

## Licença

Este projeto está licenciado sob a MIT License.
