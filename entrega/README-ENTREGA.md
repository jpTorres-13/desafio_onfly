- primeira execução do `pytest` (registrada em `log/0.txt`) para direcionamento das intervenções

- identificada raiz das operações em `src/onfly_report/services/report_builder.py`

- análise linha a linha de `src/onfly_report/services/report_builder.py:build`

- identificação e intervenção incremental sobre os erros

    - `src/onfly_report/services/status_policy.py:is_billable`
    > assumia apenas CANCELADO como status não faturável
    > identificada divergência com as instruções
    > corrigida verificação para assumir apenas CONFIRMADO como status faturável

    - `src/onfly_report/services/stay_calculator.py:calculate_room_nights`
    > calculava diferença entre os dias das datas antes de multiplicar pela quantidade de quartos
    > identificada divergência com as instruções
    > corrigida para calcular a diferença de dias entre as datas para então multiplicar pela quantidade de quartos

    - `src/onfly_report/services/currency_converter.py:convert_to_brl`
    > calculava conversão pela divisão do montante pela taxa de conversão da moeda correspondente
    > identificada divergência com as instruções
    > corrigida para calcular a conversão pela multiplicação o montante pela taxa de conversão da moeda correspondente em função da taxa de conversão da moeda de destino (precaução)

- segunda execução do `pytest` (registrada em `log/1.txt`) para avaliação das intervenções realizadas

- sequência na análise linha a linha de `src/onfly_report/services/report_builder.py:build`

- sequência na identificação e intervenção incremental sobre os erros restantes

    - `src/onfly_report/services/report_builder.py:91`
    > ordenava dicionário pelo montante em ordem crescente
    > identificada divergência com as instruções
    > corrigido para ordenar dicionário pelo oposto do montante em ordem crescente (ordem prática decrescente), sem alterar fator de ordenação do termo de desempate

- terceira execução do `pytest` (registrada em `log/2.txt`) para avaliação das intervenções realizadas

**intervenções comentadas no código**
