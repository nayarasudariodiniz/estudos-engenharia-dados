![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=flat&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

# Análise de Dados E-commerce Olist (2016-2018)

Este projeto realiza uma análise exploratória e estrutural dos dados de vendas da Olist, focando em performance financeira, comportamento temporal e integração de múltiplas fontes de dados para extração de insights estratégicos.

## 🚀 Como Executar o Projeto

Para reproduzir esta análise, siga os passos abaixo:

1.  **Dados:** Baixe os arquivos originais diretamente do [Kaggle - Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
2.  **Banco de Dados:** Execute o script de criação do banco de dados SQL para consolidar os arquivos CSV em tabelas relacionais.
3.  **Dependências:** Certifique-se de ter as bibliotecas instaladas:
    ```bash
    pip install pandas matplotlib numpy sqlite3
    ```

## 🛠️ Tecnologias e Conceitos Aplicados

* **I/O de Dados:** Integração entre SQL, CSV e dicionários de tradução utilizando as ferramentas de IO do Pandas (`read_sql`, `read_csv`).
* **ETL e Limpeza:** Tratamento de tipos de dados, conversão de Timestamps e gestão de dados nulos ou infinitos.
* **Data Storytelling:** Visualização de dados avançada com Matplotlib para comunicação de resultados executivos.

---

## 🧠 Aprendizados de Percurso (Insights Técnicos)

Durante o desenvolvimento, desafios reais de engenharia e análise de dados foram superados:

### 1. Integridade Temporal e Slicing
* **Preservação do Raw Data:** Identificou-se que a extração precoce de componentes da data (ano/mês) limitava o uso de funções de `resample`. A solução foi preservar o timestamp original durante os merges para garantir a integridade das séries temporais. 
* **Ordenação (Monotonic Index):** Para realizar cortes temporais (slicing) sem erros de `KeyError`, aplicamos o `.sort_index()`, garantindo que o índice de tempo estivesse em ordem cronológica antes de qualquer filtragem.

### 2. Visualização e Escala Financeira
* **Faturamento vs. Crescimento:** Enquanto o faturamento absoluto mostra o tamanho do negócio, aplicamos o método `.pct_change()` para observar o ritmo (Month-over-Month). Isso revelou comportamentos sazonais, como a "ressaca" de vendas após a Black Friday.
* **Data Formatting:** Eliminamos a notação científica (`1e6`) nos eixos utilizando o `ticker.FuncFormatter`, convertendo valores brutos para o padrão monetário brasileiro (R$). Também utilizamos `mdates.DateFormatter` para limpar a visualização do eixo cronológico.

### 3. Integração e Tradução
* Utilizamos a tabela de tradução de categorias para enriquecer a base de itens, permitindo que as visualizações finais utilizassem nomenclaturas padronizadas e amigáveis ao negócio.

---

## 📈 Resultados e Visualizações

O projeto consolida análises sobre:
* **Evolução Mensal:** Comparativo entre volume de pedidos e receita total.
* **Taxa de Crescimento (MoM%):** Identificação de picos de demanda e períodos de retração.
* **Top 10 Categorias:** Ranking das categorias que mais geram faturamento para a plataforma.

---

## 📁 Versionamento e Segurança

* **Git Workflow:** O projeto utiliza versionamento semântico para documentar a evolução das etapas de ETL.
* **Segurança:** Arquivos volumosos (`.csv`, `.db`) e ambientes virtuais (`.venv`) são ignorados via `.gitignore`, mantendo o repositório leve e focado apenas no código e documentação.

---
*Projeto desenvolvido como parte do portfólio de Engenharia e Análise de Dados.*