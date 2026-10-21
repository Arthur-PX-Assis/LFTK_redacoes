import pandas as pd

# Carrega a planilha gerada
df = pd.read_excel('data/redacoes_enem.xlsx')

total_linhas = len(df)
nomes_colunas = df.columns.tolist()
limites = [0, 200, 400, 600, 800, 1000]
df['intervalo_nota'] = pd.cut(df['score'], bins=limites, include_lowest=True)
contagem_agrupada = df['intervalo_nota'].value_counts().sort_index()
contagem_scores = df['score'].value_counts().sort_index()

print(f"Total de linhas: {total_linhas}")
print(f"Nomes das colunas: {nomes_colunas}")
print(f"\nComeço do df:\n{df.head()}")
print(f"\nQuantidade de redações por faixa de nota:\n{contagem_agrupada}")
print(f"\nQuantidade de redações por nota:\n{contagem_scores}")
