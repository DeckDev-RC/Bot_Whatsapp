import pandas as pd

# Carrega a planilha Excel
df = pd.read_excel("Bolo.xlsx")

#Quantidade de itens por pessoas
total = df["Total"].loc[0:48].astype(str).tolist()

# Criar lista com os nomes para mensagem
nomes = df["Nomes"].loc[0:48].astype(str).tolist()

# Cria uma lista com os nomes
contatos = df["Nome"].loc[0:48].astype(str).tolist()

# Cria uma lista com os valores devidos
mensagem = df["Valor a Pagar"].loc[0:48].astype(str).tolist()

# Cria um dicionário para armazenar os itens
total_list=[]
nomes_list =[]
contatos_list = []
mensagens_list = []

# Itera sobre os nomes e os valores devidos
for contatos, mensagem, nomes, total in zip(contatos, mensagem, nomes, total):
    # Adiciona o nome e o valor devido ao dicionário
    total_list.append(total)
    nomes_list.append(nomes)
    contatos_list.append(contatos)
    mensagens_list.append(mensagem)

# Imprime o dicionário
print(total_list)
print(nomes_list)
print(contatos_list)
print(mensagens_list)
