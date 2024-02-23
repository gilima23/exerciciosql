#Fazendo conexão com o Banco de Dados 

import sqlite3 

exerciciosql = sqlite3.connect('banco2')
cursor = exerciciosql.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (1, "Giovana", 20, "Gestão da Informação")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (2, "Ana", 21, "Engenharia da Computação")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (3, "Pedro", 18, "Arquitetura")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (4, "Carlos", 25, "Letras")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (5, "João", 22, "Design")')

#3.Consultas Básicas: Escreva consultas SQL para realizar as seguintes tarefas:

#a) Selecionar todos os registros da tabela "alunos".
#alunos = cursor.execute('SELECT * FROM alunos')
#for aluno in alunos:
    #print(aluno)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
#alunos = cursor.execute('SELECT idade,nome FROM alunos WHERE idade > 20')
#for aluno in alunos:
    #print(aluno)   

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.    

#Adicionando alunos que cursam engenharia para visualizar a ordem alfabetica

#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (6, "Paulo", 22, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (7, "Maria", 22, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (8, "João", 22, "Engenharia")')

#alunos =cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
#for aluno in alunos:
    #print(aluno)

#d) Contar o número total de alunos na tabela
#cursor.execute('SELECT COUNT(*) AS total_alunos FROM alunos')
#resultado = cursor.fetchone()
#total_alunos = resultado[0]
#print("O total de alunos na tabela é:", total_alunos)

#4.Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
#cursor.execute('UPDATE alunos SET idade = 25 WHERE id = 1')

#b) Remova um aluno pelo seu ID.
#cursor.execute('DELETE FROM alunos WHERE id = 3')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
#registros de clientes na tabela.

#Criando a tabela
#cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

#Adicionando dados na tabela
#cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, 'João', 30, 1000.50)")
#cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, 'Maria', 25, 1500.75)")
#cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, 'Pedro', 35, 2000.00)")
#cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, 'Ana', 28, 1800.25)")

#6. Consultas e Funções Agregadas Escreva consultas SQL para realizar as seguintes tarefas:

#a)Selecione o nome e a idade dos clientes com idade superior a 30 anos.
#clientes =cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
#for cliente in clientes:
   #print(cliente)  

#b)Calcule o saldo médio dos clientes.
#cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')
#resultado = cursor.fetchone()
#saldo_medio = resultado[0]
#print("O saldo médio dos clientes é:", saldo_medio)

#c) Encontre o cliente com o saldo máximo.
#cursor.execute('SELECT nome, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
#resultado = cursor.fetchone()
#nome_cliente_max_saldo = resultado[0]
#saldo_max = resultado[1]
#print("O cliente com o saldo máximo é:", nome_cliente_max_saldo)
#print("Saldo máximo:", saldo_max)

#d)Conte quantos clientes têm saldo acima de 1000.
#cursor.execute('SELECT COUNT(*) AS total_clientes FROM clientes WHERE saldo > 1000')
#resultado = cursor.fetchone()
#total_clientes_saldo_acima_1000 = resultado[0]
#print("Total de clientes com saldo acima de 1000:", total_clientes_saldo_acima_1000)

#7. Atualização e Remoção com Condições

#a)Atualize o saldo de um cliente específico.
#cursor.execute('UPDATE clientes SET saldo = 2500.00 WHERE id = 1')

#b)Remova um cliente pelo seu ID.
#cursor.execute('DELETE FROM clientes WHERE id = 2')

#8.Junção de Tabelas 
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

#Criando a tabela

#cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY,cliente_id INT, produto VARCHAR(100),valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES clientes(id))'),

#Inserindo compras associadas a clientes existentes na tabela "clientes

#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 1, "arroz", 5.50)')
#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 3, "feijao", 8.00)')
#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 4, "carne", 20.00)')
#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (4, 3, "banana", 3.50)')

#Escrevendo uma consulta para exibir nome do cliente, produto e valor de compra 
#dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.cliente_id = clientes.id')
#for usuario in dados:
   #print(usuario)





exerciciosql.commit() 
exerciciosql.close()