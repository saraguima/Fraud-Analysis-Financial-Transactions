import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../../../data/paysim.csv')

# Histograma dos valores das transações (escala log)
plt.figure(figsize=(8,5))
sns.histplot(data=df, x='amount', hue='isFraud', bins=50,
             log_scale=True, palette=['#2ecc71', '#e74c3c'], alpha=0.7)
plt.xlabel('Valor (R$) - escala logarítmica')
plt.ylabel('Quantidade')
plt.legend(title='Fraude', labels=['Legítima', 'Fraude'])
plt.tight_layout()

plt.savefig('fig2_valores_transacao.png')
plt.close()
print("Gráfico 2 gerado: fig2_valores_transacao.png")
