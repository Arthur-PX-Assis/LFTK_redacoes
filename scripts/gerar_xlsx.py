from external.build_dataset import Corpus

c = Corpus()
train, valid, test = c.read_splits(path='external/essay-br/splits')

dados_exportacao = train[['essay', 'score', 'competence']].copy()
dados_exportacao['essay'] = dados_exportacao['essay'].apply(lambda x: ' '.join(x))
dados_exportacao['competence'] = dados_exportacao['competence'].astype(str)
dados_exportacao.to_excel('data/redacoes_enem.xlsx', index=False)

print("Arquivo salvo com sucesso!")