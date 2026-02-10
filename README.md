# 📦 E-Commerce Data Pipeline & Analysis (Olist)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=flat&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20constru%C3%A7%C3%A3o-orange)

Este projeto simula um ambiente real de Engenharia de Dados, utilizando o dataset público da **Olist** (maior marketplace do Brasil). O objetivo é transformar dados brutos em inteligência de negócio através de uma arquitetura relacional.

## 🚀 Status do Projeto
O projeto está atualmente na fase de **Análise Exploratória e Limpeza de Dados**. As próximas etapas incluem modelagem avançada (Joins/Merges) e visualização de dados.

## 📋 Pré-requisitos & Instalação

> **⚠️ IMPORTANTE:** Para garantir a integridade das análises, siga os passos abaixo:
> 1. Realize o download dos arquivos brutos diretamente no [Kaggle da Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
> 2. Execute o script de criação do banco de dados (SQL) disponível na pasta `scripts/` para gerar o arquivo `olist.db`.

## 🛠️ Tecnologias Utilizadas
- **Python**: Linguagem core para manipulação.
- **Pandas**: Biblioteca principal para análise de dados.
- **SQLite**: Banco de dados relacional para armazenamento e consultas SQL.
- **VS Code + Jupyter Notebooks**: Ambiente de desenvolvimento.

## 📈 Evolução do Trabalho (Log de Atividades)
Até o momento, o pipeline contempla:
1. **Configuração de Ambiente**: Uso de ambientes virtuais (`.venv`) e conexão com SQLite.
2. **Extração via SQL**: Consultas de faturamento e volumetria direto do banco de dados.
3. **Data Cleaning**: Tratamento crítico de valores nulos (imputação por mediana e valores constantes) em vez de exclusão.
4. **Análise Multidimensional**: Implementação de `MultiIndex` e `Cross-section (xs)` para entender o faturamento por Estado e Categoria.
5. **Estatística Descritiva**: Uso de agrupamentos complexos para cálculo de Ticket Médio e Desvio Padrão.

---
✨ *Este projeto está sendo desenvolvido como parte do meu portfólio de Engenharia de Dados.*
