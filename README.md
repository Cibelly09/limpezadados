<div align="center">

# 🐍 Projeto Python — Análise Exploratória do Eleitorado com Deficiência

<img width="500" src="https://github.com/Cibelly09/imagens_portfolio/raw/main/python_header.png">

Análise exploratória, limpeza, padronização e visualização dos dados de eleitores com deficiência, utilizando Python, Pandas, Matplotlib, Seaborn e Plotly.

---

### 🔍 Objetivo do Projeto
Realizar uma análise exploratória detalhada sobre o perfil dos eleitores com deficiência no Brasil, identificando padrões, comportamentos e proporções relevantes para estudos eleitorais.

</div>

---

## 🧹 1. Limpeza e Preparação dos Dados

```python
df = pd.read_excel("eleitorado.xlsx", engine="openpyxl")

df_def = df[['SG_UF','QT_ELEITORES_DEFICIENCIA', 'DS_RACA_COR',
             'DS_GRAU_ESCOLARIDADE','DS_FAIXA_ETARIA',
             'DS_ESTADO_CIVIL','DS_GENERO']]

# Remove valores nulos e inválidos
df_def = df_def[df_def['QT_ELEITORES_DEFICIENCIA'].notna() &
                (df_def['QT_ELEITORES_DEFICIENCIA']>0)]

df_def = df_def[~df_def.applymap(lambda x: x in
                ['Prefere nAo informar','NAO INFORMADO','Inválida']).any(axis=1)]

