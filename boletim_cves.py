import nvdlib
import datetime
import pandas as pd
import plotly.express as px
from jinja2 import Environment, FileSystemLoader

# Função para obter a data atual e uma semana atrás
def get_date_range():
    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=7)
    return start, end

# Função para buscar CVEs da API NVD
def fetch_cves(start, end):
    try:
        # Chave da API NVD deve ser configurada corretamente
        results = nvdlib.searchCVE(cvssV3Severity='', pubStartDate=start, pubEndDate=end, key='SUA-CHAVE-NVD', delay=50)
        if not results:
            print("Nenhuma CVE encontrada.")
        return results
    except Exception as e:
        print(f"Erro ao buscar CVEs: {e}")
        return []

# Função para extrair cveID e description de cada CVE
def extract_cve_data(result):
    cve_id = getattr(result, 'id', 'ID não disponível')  # Tente acessar o atributo 'id'
    description = None
    if hasattr(result, 'descriptions') and result.descriptions:
        description = result.descriptions[0].value  # Pegue a primeira descrição disponível
    else:
        description = 'Descrição não disponível'
    
    return {'cveID': cve_id, 'description': description}

# Função para agrupar CVEs por severidade
def group_cves_by_severity(results):
    critical, high, medium, low = [], [], [], []

    for result in results:
        cve_data = extract_cve_data(result)
        v30score = getattr(result, 'v30score', None)
        v31score = getattr(result, 'v31score', None)

        if (v30score and v30score >= 9.0) or (v31score and v31score >= 9.0):
            critical.append(cve_data)
        elif (v30score and 7.0 <= v30score <= 8.9) or (v31score and 7.0 <= v31score <= 8.9):
            high.append(cve_data)
        elif (v30score and 4.0 <= v30score <= 6.9) or (v31score and 4.0 <= v31score <= 6.9):
            medium.append(cve_data)
        else:
            low.append(cve_data)

    return critical, high, medium, low

# Função para criar o gráfico de severidades
def create_severity_chart(critical, high, medium, low):
    df = pd.DataFrame({
        'Severidade': ['Critical', 'High', 'Medium', 'Low'],
        'Quantidade': [len(critical), len(high), len(medium), len(low)]
    })

    # Definindo as cores personalizadas para cada severidade
    colors = ['#800080', '#FF0000', '#FFA500', '#FFFF00']  # Roxo, Vermelho, Laranja, Amarelo

    # Criando o gráfico com as cores personalizadas
    fig = px.bar(df, x='Severidade', y='Quantidade', title='Total de Vulnerabilidades por Severidade',
                 color='Severidade', color_discrete_sequence=colors)

    return fig

# Função para gerar o relatório em HTML
def generate_html_report(critical, high, medium, low, fig_html):
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template('dashboard.html')

    output = template.render(
        critical=critical,
        high=high,
        medium=medium,
        low=low,
        fig=fig_html
    )

    with open("./Boletim CVEs/Boletim_CVE.html", "w") as file:
        file.write(output)
    print("Arquivo HTML gerado com sucesso.")

# Função principal que coordena a execução do script
def main():
    start, end = get_date_range()
    results = fetch_cves(start, end)

    if results:
        critical, high, medium, low = group_cves_by_severity(results)
        fig = create_severity_chart(critical, high, medium, low)
        fig_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

        generate_html_report(critical, high, medium, low, fig_html)

if __name__ == '__main__':
    main()
