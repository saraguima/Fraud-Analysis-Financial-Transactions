# Fraud Analysis in Financial Transactions Using the Synthetic Financial Dataset For Fraud Detection

## ➔ Contexto Acadêmico
Este repositório contém contém os códigos, análises e resultados do artigo científico desenvolvido na disciplina **Sistemas de Informação Integrada**, no 7º semestre de **Sistemas de Informação**.
O estudo segue a metodologia científica orientada pela disciplina e adota o modelo de artigo acadêmico no padrão **ACM (sigconf)**.


## ➔ Objetivo 
Propor e avaliar técnicas de Machine Learning para detecção de fraudes financeiras, utilizando diferentes algoritmos e estratégias de balanceamento de dados.

---

## ➔ Estrutura do Artigo

### 1. Introdução
A detecção de fraudes em transações financeiras é um dos maiores desafios enfrentados por instituições bancárias e empresas de tecnologia.  
Este artigo tem como objetivo **avaliar modelos de aprendizado de máquina supervisionados** aplicados à base **PaySim**, um dataset sintético de transações financeiras.

- **Problema de pesquisa:** Como diferentes algoritmos de classificação binária se comportam na identificação de fraudes em transações financeiras?  
- **Objetivo geral:** Analisar o desempenho de técnicas de aprendizado supervisionado na detecção de fraudes.  
- **Objetivos específicos:**  
  - Pré-processar e preparar os dados para análise;  
  - Construir modelos de classificação (Random Forest e XGBoost);  
  - Avaliar os resultados com métricas apropriadas;  
  - Comparar o desempenho dos modelos;  
  - Discutir limitações e oportunidades de melhoria.  

A importância do trabalho está na **relevância prática** para sistemas antifraude e na **contribuição científica** para estudos sobre classificação em bases desbalanceadas.

---

### 2. Descrição da Base de Dados
- **Nome:** Synthetic Financial Datasets For Fraud Detection (PaySim)  
- **Fonte:** [Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1/data)  
- **Estrutura:** ~6,3 milhões de registros com variáveis de transações financeiras.  
- **Variável-alvo:** `isFraud` (0 = transação legítima, 1 = fraude).  
- **Domínio da aplicação:** Organizacional e tecnológico, aplicado a sistemas de informação e segurança bancária.  


⚠️ **Atenção:** A base não está incluída neste repositório. Para reproduzir os experimentos:
1. Baixe os dados no link acima.
2. Coloque o arquivo CSV dentro da pasta `data/`.

---

### 3. Tratamentos Preliminares e Engenharia de Dados
Foram aplicados os seguintes tratamentos:  
- Remoção de colunas irrelevantes e redundantes;  
- Normalização de valores monetários;  
- Criação de variáveis derivadas para capturar padrões de fraude;  
- Balanceamento da base por meio da técnica **SMOTE** (Synthetic Minority Oversampling Technique).  

Essas escolhas foram realizadas para garantir que os algoritmos tivessem condições adequadas de treinamento, dada a alta desproporção entre transações legítimas e fraudulentas.

---

### 4. Análise Estatística e Visualização de Dados
Foram geradas estatísticas descritivas e gráficos para compreender a distribuição das variáveis e padrões de fraude.  
Entre os principais **insights**:  
- A maior parte das transações fraudulentas está concentrada em determinados tipos de operação financeira;  
- Existe um desbalanceamento extremo entre transações legítimas e fraudulentas (menos de 1% são fraudes).  

📊 Exemplos de gráficos disponíveis na pasta [`results/graficos`](./results/graficos).

---

### 5. Modelagem e Classificação
Foram construídos e avaliados dois modelos principais:  
- **Random Forest**  
- **XGBoost**

#### Métricas de avaliação utilizadas:
- Acurácia  
- Precisão  
- Recall  
- F1-score  
- Matriz de confusão

➔ Os resultados mostraram que:  
- O **Random Forest** apresentou bom desempenho geral, mas sofreu com recall baixo em fraudes.  
- O **XGBoost**, após ajustes de hiperparâmetros, obteve melhor equilíbrio entre precisão e recall, sendo mais indicado para problemas com classes desbalanceadas.  

---

### 6. Conclusão
O estudo atingiu os objetivos propostos ao comparar dois modelos supervisionados aplicados à detecção de fraudes financeiras.  
Os resultados evidenciam:  
- A necessidade de técnicas de balanceamento (como SMOTE) para evitar viés de classificação;  
- O potencial do **XGBoost** como modelo robusto para problemas desbalanceados;  
- A importância da visualização e análise estatística como etapas fundamentais para compreender os dados antes da modelagem.  

**Trabalhos futuros** podem incluir:  
- Testar outros algoritmos (como Redes Neurais e SVM);  
- Aplicar técnicas de explicabilidade (SHAP, LIME) para entender as decisões dos modelos;  
- Ampliar a análise para diferentes bases financeiras.  

---

## ➔ Estrutura do Repositório
fraud-analysis-financial-transactions/
│── README.md <- Este documento
│── artigo/ <- Artigo completo em PDF (modelo ACM)
│── data/ <- Dataset (não incluído por licença)
│── src/ <- Scripts de pré-processamento, visualização e modelagem
│── results/ <- Gráficos e resultados gerados
│── requirements.txt <- Dependências do projeto

---

** ➔ Tecnologias Utilizadas**:
- Python 3.10+
- Pandas, Numpy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Matplotlib, Seaborn
- XGBoost


➨ **Autores:** Alan Keizo F. Katsuyama, Felipe Vieira Fernandes, Gabriel Rodrigues Araujo, Sara Guimarães Souza (2025)  
➨ **Disciplina:** Sistemas de Informação Integrada – Curso de Sistemas de Informação (UNIP, 2025)
