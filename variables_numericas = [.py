import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/retailmax.csv')

variables_numericas = [
    'Age',
    'Annual Income (k$)',
    'Spending Score (1-100)'
]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for eje, columna in zip(axes, variables_numericas):
    sns.boxplot(y=df[columna], ax=eje, color='skyblue')
    eje.set_title(f'Valores atípicos: {columna}')
    eje.set_ylabel(columna)

plt.tight_layout()
plt.show()

for columna in variables_numericas:
    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)
    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    valores_atipicos = df[
        (df[columna] < limite_inferior) |
        (df[columna] > limite_superior)
    ]

    print(f'{columna}: {len(valores_atipicos)} valores atípicos')