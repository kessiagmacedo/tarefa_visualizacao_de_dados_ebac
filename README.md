Tarefa do curso: Profissão Cientista de Dados M10 Pratique.
(Módulo visualização de dados).
# Análise e Visualização de Dados de E-commerce 📊

Este projeto faz parte de uma sequência de exercícios de tratamento e análise de dados. O objetivo principal é realizar a limpeza de uma base de dados de e-commerce e gerar visualizações estatísticas para extrair insights valiosos sobre produtos, preços e avaliações.

## 🚀 Tecnologias Utilizadas

* **Python 3.x**
* **Pandas**: Manipulação e limpeza de dados.
* **Matplotlib**: Criação de gráficos base.
* **Seaborn**: Visualizações estatísticas avançadas e estéticas.

## 📋 Requisitos da Tarefa

O script processa o arquivo `ecommerce_estatistica.csv` e gera as seguintes visualizações:

1.  **Histograma**: Distribuição de preços.
2.  **Dispersão**: Relação entre Preço e Volume de Avaliações.
3.  **Mapa de Calor**: Correlação entre todas as variáveis numéricas.
4.  **Gráfico de Barras**: Preço médio por material (Top 10).
5.  **Gráfico de Pizza**: Representatividade por Gênero (com detalhamento de nichos).
6.  **Gráfico de Densidade**: Probabilidade de distribuição de preços.
7.  **Gráfico de Regressão**: Tendência entre Preço e Nota do Produto.

## 🛠️ Tratamentos Realizados

Para garantir a qualidade dos gráficos, o código executa:
* Preenchimento de valores nulos em colunas de texto com "Não Definido".
* Tratamento de preços ausentes utilizando a **mediana**.
* Tratamento de notas ausentes utilizando a **média**.
* Normalização de colunas de métricas específicas (zerando valores nulos).

## 📈 Como Executar

1. Certifique-se de ter o arquivo `ecommerce_estatistica.csv` no mesmo diretório.
2. Instale as dependências:
   ```bash
   pip install pandas matplotlib seaborn
