

# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. Carregar a base reduzida
# ============================================================
df = pd.read_csv("perfil_eleitor_red.csv")

print("\n===== VISÃO GERAL DA BASE =====")
print(df.head())
print(df.info())

# ============================================================
# 2. Limpeza da base
# ============================================================

# Remover linhas completamente vazias, se houver
df = df.dropna(how="all")

# Converter texto para maiúsculas
df = df.applymap(lambda x: x.upper() if isinstance(x, str) else x)

# Remover valores indesejados
valores_invalidos = ["PREFERE NAO INFORMAR", "NAO INFORMADO", "INVÁLIDA", "INVALIDA"]

df = df[~df.applymap(lambda x: x in valores_invalidos).any(axis=1)]

print("\n===== BASE APÓS LIMPEZA =====")
print(df.info())
print(df.head())

# ============================================================
# 3. Gráficos de barras
# ============================================================

def save_barplot(series, title, filename, rotation=45):
    """
    Cria e salva um gráfico de barras simples.
    """
    counts = series.value_counts().sort_index()
    plt.figure(figsize=(10,6))
    plt.bar(counts.index.astype(str), counts.values)
    plt.title(title)
    plt.xlabel(series.name)
    plt.ylabel("Contagem")
    plt.xticks(rotation=rotation, ha='right')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# ============================================================
# 4. Gráficos descritivos
# ============================================================

print("\nGerando gráficos...")

save_barplot(
    df["DS_GENERO"],
    "Distribuição por Gênero",
    "grafico_genero.png"
)

save_barplot(
    df["DS_FAIXA_ETARIA"],
    "Distribuição por Faixa Etária",
    "grafico_faixa_etaria.png"
)

save_barplot(
    df["DS_RACA_COR"],
    "Distribuição por Raça/Cor",
    "grafico_raca.png"
)

save_barplot(
    df["DS_GRAU_ESCOLARIDADE"],
    "Distribuição por Escolaridade",
    "grafico_escolaridade.png"
)

save_barplot(
    df["DS_ESTADO_CIVIL"],
    "Distribuição por Estado Civil",
    "grafico_estado_civil.png"
)

save_barplot(
    df["SG_UF"],
    "Distribuição por Estado (UF)",
    "grafico_uf.png"
)

print("\n===== GRÁFICOS GERADOS COM SUCESSO! =====")
print("Arquivos PNG foram salvos na pasta local.")


