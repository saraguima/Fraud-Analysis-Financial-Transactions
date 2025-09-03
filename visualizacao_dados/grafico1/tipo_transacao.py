import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dataset (ajuste o caminho se necessário)
df = pd.read_csv('../../../../data/paysim.csv')

# Gráfico: Distribuição dos tipos de transação
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='type', order=df['type'].value_counts().index, palette='viridis')
plt.xlabel('Tipo de Transação')
plt.ylabel('Frequência')
plt.tight_layout()

# Salvar gráfico na mesma pasta
plt.savefig('fig1_tipo_transacao.png')
plt.close()

print("Gráfico 1 gerado: fig1_tipo_transacao.png")
