import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from external.build_dataset import Corpus

raiz_projeto = os.getcwd()

try:
    os.chdir('external')
    
    c = Corpus()
    train, valid, test = c.read_splits()
finally:
    os.chdir(raiz_projeto)

df_completo = pd.concat([train, valid, test], ignore_index=True)

dados_exportacao = df_completo[['essay', 'score', 'competence']].copy()
dados_exportacao['essay'] = dados_exportacao['essay'].apply(lambda x: ' '.join(x))
dados_exportacao['competence'] = dados_exportacao['competence'].astype(str)

dados_exportacao.to_excel('data/redacoes_enem.xlsx', index=False)
print(f"Arquivo salvo com sucesso! Total de redações consolidadas: {len(dados_exportacao)}")