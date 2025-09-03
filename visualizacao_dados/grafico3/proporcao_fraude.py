import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../../../data/paysim.csv')

fraud_counts = df['isFraud'].value_counts()
colors = ['#2ecc71', '#e74c3c']

plt.figure(figsize=(6,6))
patches, texts, autotexts = plt.pie(
    fraud_counts,
    labels=['Legítima', 'Fraude'],
    autopct='%1.2f%%',
    colors=colors,
    startangle=90,
    textprops={'color':'white','weight':'bold'}
)

plt.legend(patches, ['Não Fraude', 'Fraude'], loc='upper right', title='Tipo de Transação')
plt.tight_layout()
plt.savefig('fig3_proporcao_fraude.png')
plt.close()
print("Gráfico 3 gerado: fig3_proporcao_fraude.png")
