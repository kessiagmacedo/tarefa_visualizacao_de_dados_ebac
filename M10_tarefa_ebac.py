import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. LEITURA DOS DADOS
# Alterado para o nome do arquivo solicitado na tarefa
df = pd.read_csv('ecommerce_limpo.csv')

# 2. TRATAMENTO DE DADOS (DATA CLEANING)
# Tratando colunas de texto
colunas_texto = ['Material', 'Gênero', 'Review1', 'Review2', 'Review3']
for colunas in colunas_texto:
    if colunas in df.columns:
        df[colunas] = df[colunas].fillna('Não Definido')

# Tratando valores numéricos (Média e Mediana)
df['Preço'] = df['Preço'].fillna(df['Preço'].median())
df['Nota'] = df['Nota'].fillna(df['Nota'].mean())

# Zerando colunas específicas de métricas
colunas_para_zerar = ['Nota_MinMax', 'N_Avaliações', 'N_Avaliações_MinMax',
                      'Desconto_MinMax', 'Preço_MinMax', 'Qtd_Vendidos_Cod',
                      'Material_Freq', 'Desconto']

for colunas_zeros in colunas_para_zerar:
    if colunas_zeros in df.columns:
        df[colunas_zeros] = df[colunas_zeros].fillna(0)

# Configuração visual do Seaborn
sns.set_theme(style="whitegrid")

# --- 3. VISUALIZAÇÕES ---

# A. GRÁFICO DE HISTOGRAMA
plt.figure(figsize=(10, 5))
sns.histplot(df['Preço'], kde=False, color='skyblue')
plt.title('Gráfico de Histograma: Distribuição de Preços')
plt.xlabel('Preço (R$)')
plt.ylabel('Frequência')
plt.show()

# B. GRÁFICO DE REGRESSÃO
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Preço', y='Nota', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Gráfico de Regressão: Relação entre Preço e Nota')
plt.xlabel('Preço (R$)')
plt.ylabel('Nota do Cliente')
plt.show()

# C. MAPA DE CALOR (HEATMAP)
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Mapa de Calor: Correlação entre Variáveis')
plt.xticks(rotation=45, ha='right')
plt.show()

# D. GRÁFICO DE BARRA
top_materiais = df['Material'].value_counts().nlargest(10).index
df_top = df[df['Material'].isin(top_materiais)]

plt.figure(figsize=(10, 6))
sns.barplot(data=df_top, x='Preço', y='Material', estimator='mean', errorbar=None, palette='viridis')
plt.title('Gráfico de Barra: Preço Médio por Material (Top 10)')
plt.xlabel('Preço Médio (R$)')
plt.ylabel('Material')
plt.show()

# E. GRÁFICO DE DISPERSÃO (SCATTER PLOT)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Preço', y='N_Avaliações', alpha=0.6, color='teal')
plt.title('Gráfico de Dispersão: Preço vs. Número de Avaliações')
plt.xlabel('Preço (R$)')
plt.ylabel('Quantidade de Avaliações')
plt.show()

# F. GRÁFICO DE PIZZA (E DETALHAMENTO)
contagem = df['Gênero'].value_counts()
total = contagem.sum()
porcentagens = (contagem / total) * 100

maiores = contagem[porcentagens >= 5]
menores = contagem[porcentagens < 5]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Gráfico de Pizza principal
labels_maiores = [f'{l}\n({s/total*100:1.1f}%)' for l, s in zip(maiores.index, maiores.values)]
ax1.pie(maiores, labels=labels_maiores, startangle=140, colors=sns.color_palette('pastel'), wedgeprops={'edgecolor': 'white'})
ax1.set_title('Gráfico de Pizza: Gêneros Principais (> 5%)', fontsize=14)

# Barras para detalhar os menores (evita poluição no gráfico de pizza)
sns.barplot(x=menores.values, y=menores.index, ax=ax2, palette='magma')
ax2.set_title('Detalhe: Gêneros com Baixa Representatividade', fontsize=14)
ax2.set_xlabel('Quantidade de Produtos')

plt.tight_layout()
plt.show()

# G. GRÁFICO DE DENSIDADE (KDE)
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color="orange", bw_adjust=0.5)
plt.title('Gráfico de Densidade: Probabilidade de Preços')
plt.xlabel('Preço (R$)')
plt.ylabel('Densidade')
plt.show()