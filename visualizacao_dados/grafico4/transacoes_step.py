import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../../../../data/paysim.csv')

df_step = df.groupby('step').size().reset_index(name='Quantidade')

plt.figure(figsize=(10,5))
sns.lineplot(data=df_step, x='step', y='Quantidade', color='#3498db')
plt.xlabel('Step (unidade de tempo)')
plt.ylabel('Quantidade de transações')
plt.tight_layout()

plt.savefig('fig4_transacoes_step.png')
plt.close()
print("Gráfico 4 gerado: fig4_transacoes_step.png")
