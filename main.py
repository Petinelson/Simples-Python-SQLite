import sqlite3
import os

# Função para limpar a tela
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def conectar():
    return sqlite3.connect('banco.db')

def inicializar_banco():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_cadastro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            cargo TEXT NOT NULL
        )
    ''')
    conexao.commit()
    cursor.close()
    conexao.close()

def inserir():
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    cargo = input("Digite o cargo: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tb_cadastro (nome, email, cargo) VALUES (?,?,?)", (nome, email, cargo))
    conexao.commit()
    print("Dados inseridos com sucesso.")
    cursor.close()
    conexao.close()

def listar():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tb_cadastro")
    for linha in cursor.fetchall():
        print(linha)
    cursor.close()
    conexao.close()

def atualizar():
    id = input("Digite o id do cadastro que deseja atualizar: ")
    nome = input("Digite o novo nome: ")
    email = input("Digite o novo email: ")
    cargo = input("Digite o novo cargo: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE tb_cadastro SET nome=?, email=?, cargo=? WHERE id=?", (nome, email, cargo, id))
    conexao.commit()
    print("Dados atualizados com sucesso.")
    cursor.close()
    conexao.close()

def excluir():
    id_ = input("Digite o id do cadastro que deseja excluir: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tb_cadastro WHERE id=?", (id_,))
    conexao.commit()
    print("Cadastro excluído com sucesso.")
    cursor.close()
    conexao.close()

def menu():
    inicializar_banco()  # Chama a função para inicializar o banco de dados e a tabela, se necessário
    while True:
        limpa_tela()
        print("\nMENU")
        print("1 - Inserir novo cadastro")
        print("2 - Listar cadastros")
        print("3 - Atualizar cadastro")
        print("4 - Excluir cadastro")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            atualizar()
        elif opcao == '4':
            excluir()
        elif opcao == '5':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

        print("Pressione Enter para continuar...")
        input()
        
        
menu()
