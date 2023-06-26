#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('reset', '')


# In[31]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#descobrir o quanto a média dos 10 diretores que estão no topo descia da média geral


# In[18]:


#Introdução:

#O campo da Data Science tem se tornado cada vez mais relevante para a análise e compreensão de dados em diversos setores, incluindo a indústria cinematográfica. Neste trabalho, exploraremos um conjunto de dados que contém informações sobre filmes, diretores, atores e suas respectivas avaliações.

#Ao analisar esses dados, abordaremos diferentes questões em relação à relação entre as variáveis disponíveis. Primeiramente, investigaremos se existe uma relação entre o diretor de um filme e sua avaliação (rating). Será que diretores específicos têm uma tendência a produzir filmes com melhores avaliações? Essa análise nos ajudará a compreender se a direção de um filme está correlacionada com sua qualidade percebida.

#Além disso, examinaremos se a estrela principal (star1) de um filme tem influência sobre sua avaliação. Será que filmes com determinados atores ou atrizes como protagonistas tendem a receber classificações mais altas? Essa análise nos permitirá investigar se a popularidade ou habilidade do ator/atriz principal pode afetar a percepção do público em relação ao filme.

#Outro aspecto interessante a ser explorado é o rendimento monetário bruto dos filmes. Identificaremos qual filme obteve o maior rendimento bruto na amostra de dados, destacando a importância comercial do cinema. Além disso, investigaremos se há uma relação entre o rendimento monetário e a avaliação dos filmes. Será que filmes que arrecadam mais dinheiro tendem a receber melhores classificações? Essa análise nos permitirá explorar a relação entre sucesso comercial e qualidade percebida.

#Além disso, vamos descobrir qual ator ou atriz é o mais frequente no conjunto de dados, fornecendo uma visão sobre os artistas mais prolíficos ou populares presentes nos filmes analisados.

#Por fim, analisaremos a média dos 10 diretores mais bem avaliados em comparação com a média geral. Essa análise nos permitirá compreender se os diretores de destaque apresentam um desempenho significativamente superior em relação à média geral, indicando um possível padrão de excelência entre esse grupo selecionado.

#Ao investigar essas questões, esperamos obter insights valiosos sobre a indústria cinematográfica, as variáveis que a influenciam e as relações entre elas. Isso nos ajudará a compreender melhor o que contribui para o sucesso de um filme e a tomar decisões mais informadas em futuras produções.'


# In[14]:


#Verificando a base de dados
df = pd.read_csv("imdb_top_1000.csv",low_memory=False)
df.head()


# In[26]:


#Existe relação do director com o rating do filme?
#1. Verificar qual o nome de diretor + IMDB_Rating que tem maior frequência
df1 = df[["Director","IMDB_Rating"]]
frequencia_nomes = df1[['Director','IMDB_Rating']].value_counts()


#2. Descobrir os 10 primeiros nomes de diretores
frequencia_nomes.head(10)

#Conclusão
#Todas as 10 posições do ranking estão acima de 7, então a resposta é sim.


# In[34]:


#Existe relação entre o rating do filme e a star 1?
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Star1', y='IMDB_Rating')
plt.xlabel('Star1')
plt.ylabel('Rating')
plt.title('Relação entre Star1 e Rating')
plt.show()

#Estamos utilizando a biblioteca seaborn para plotar um gráfico de dispersão para visualizar a relação entre as colunas 'star1' e 'rating'. Cada ponto no gráfico representa um filme, sendo 'star1' o valor no eixo x e 'rating' o valor no eixo y.
#A concentração dos dados em uma faixa mais alta (acima de 7) sugere que os filmes em seu conjunto de dados são, em sua maioria, avaliados de forma positiva. Isso pode indicar que os filmes têm uma boa recepção e são considerados de qualidade pelos espectadores.
#A conclusão é que existe pouca rela~ção, apenas influenciando um pouco na nota positiva e acima de 7.


# In[44]:


#Filme que mais rendeu dinheiro bruto
# Converter para tipo string
df['Gross'] = df['Gross'].astype(str)

# Remover vírgulas da coluna "gross"
df['Gross'] = df['Gross'].str.replace(',', '')

# Converter para tipo float
df['Gross'] = df['Gross'].astype(float)

#Agora vamos descobrir o filme que mais rendeu
indice_filme_max_gross = df['Gross'].idxmax()
filme_max_gross = df.loc[indice_filme_max_gross]

filme_max_gross


# In[45]:


#Existe relação do rendimento monetário com o rating do filme?

# Filtrando as colunas relevantes (rendimento monetário e rating)
df_filtered = df[['Gross', 'IMDB_Rating']].dropna()

# Convertendo a coluna 'gross' para o tipo numérico
df_filtered['Gross'] = pd.to_numeric(df_filtered['Gross'], errors='coerce')

# Criando um gráfico de dispersão para visualizar a relação
plt.scatter(df_filtered['Gross'], df_filtered['IMDB_Rating'])
plt.xlabel('Rendimento Monetário')
plt.ylabel('Rating')
plt.title('Relação entre Rendimento Monetário e Rating de Filmes')
plt.show()

# Calculando a correlação entre as variáveis
correlation = df_filtered['Gross'].corr(df_filtered['IMDB_Rating'])
print('Correlação:', correlation)

#O resultado é exibido na saída, fornecendo a medida de correlação entre as variáveis.


# In[46]:


#Ator/Atriz que mais consta no dataframe

# Realizando a contagem dos atores/atrizes
contagem_atores = df['Star1'].value_counts()

# Obtendo o ator/atriz que mais aparece
ator_mais_frequente = contagem_atores.idxmax()

print('O ator/atriz que mais aparece no DataFrame é:', ator_mais_frequente)


# In[48]:


#descobrir o quanto a média dos 10 diretores que estão no topo descia da média geral

# Calculando a média geral
media_geral = df['IMDB_Rating'].mean()

# Obtendo os 10 diretores que estão no topo
top_10_diretores = df['Director'].value_counts().head(10).index.tolist()

# Filtrando o DataFrame para incluir apenas os filmes dos 10 diretores no topo
df_top_diretores = df[df['Director'].isin(top_10_diretores)]

# Calculando a média dos filmes dos 10 diretores no topo
media_top_diretores = df_top_diretores['IMDB_Rating'].mean()

# Calculando a diferença entre as médias
diferenca_media = media_top_diretores - media_geral

print('A média dos 10 diretores no topo desvia em', diferenca_media, 'da média geral.')


# In[ ]:




