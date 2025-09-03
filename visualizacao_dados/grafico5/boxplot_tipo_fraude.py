import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../../../data/paysim.csv')

plt.figure(figsize=(12,6))
sns.boxplot(data=df, x='type', y='amount', hue='isFraud', palette=['#2ecc71','#e74c3c'])
plt.yscale('log')
plt.xlabel('Tipo de Transação')
plt.ylabel('Valor (R$) - escala logarítmica')
plt.legend(title='Fraude', loc='upper right')
plt.tight_layout()

plt.savefig('fig5_boxplot_tipo_fraude.png')
plt.close()
print("Gráfico 5 gerado: fig5_boxplot_tipo_fraude.png")
