import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega o dataset 
df = pd.read_csv('../../../../data/paysim.csv')

# Documento do Artigo: Tópico 4.2 Visualização dos Dados - Pag 7

# Figura 1 — Distribuição dos tipos de transação no dataset. 
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='type', order=df['type'].value_counts().index, palette='viridis')
plt.xlabel('Tipo de Transação')
plt.ylabel('Frequência')
plt.tight_layout()

# Para visualizar: Salvar gráfico em uma pasta
plt.savefig('fig1_tipo_transacao.png')
plt.close()

print("Gráfico 1 gerado: fig1_tipo_transacao.png")
