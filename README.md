# Análise Linguística de Redações (Essay-BR + LFTK)

Este projeto tem como objetivo analisar características linguísticas (como complexidade sintática e diversidade lexical) de redações no formato ENEM. Utiliza o corpus **Essay-BR** como base de dados e a biblioteca **LFTK** para a extração de métricas, permitindo cruzar as características do texto com as notas finais e competências avaliadas.

## Estrutura do Projeto

*   **`data/`**: Contém a planilha gerada.
*   **`external/`**: Contém o código original, disponível em: https://github.com/rafaelanchieta/essay.
*   **`src/`**: Contém os módulos reutilizáveis e as abstrações de integração com o LFTK e análises estatísticas.
*   **`scripts/`**: Contém os executáveis que orquestram a transformação de dados e análises.