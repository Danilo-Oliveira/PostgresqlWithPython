import psycopg2
import time

#***************************************************************************#

#                                 Postgresql                                 #


# Faz a conexão do Python e SQL Server. ( Does the Python and SQL Server connection )
def conexao():
    con = psycopg2.connect(
        user = "dan",
        password = "1234",
        host = "localhost",
        port = "5432",
        database = "dan"
    )
    return con
    
    
#***************************************************************************#
class Users():
    def __init__(self, nome, email):
        self.nomeUser = nome
        self.emailUser = email
        
#***************************************************************************#
    def selecaoEmail(self):
        con = conexao()
        cursor = con.cursor()
        cursor.execute(f"select nome, email from users where email = '{self.emailUser}'")
        result = cursor.fetchall()
        for row in result:
            print(row[0], ' | ', row[1])
        con.commit()
        con.close()
 
       
#***************************************************************************#
    def InserirAluno(self):
        con = conexao()
        cursor = con.cursor()
        cursor.execute(f"insert into users (nome, email) values ('{self.nomeUser}', '{self.emailUser}')")
        con.commit()
        con.close()
        
#***************************************************************************#
    def AlterarInformacao(self):
        con = conexao()
        cursor = con.cursor()
        exeSQL = "update users set "
        if (self.nomeUser != ''):
            exeSQL += f"nome = '{self.nomeUser}', "
        if (self.emailUser != ''):
            exeSQL += f"email = '{self.emailUser}' "
        exeSQL = exeSQL[:-2]
        exeSQL += f"' WHERE email = '{emailAntigo}'"
        print(exeSQL)
        cursor.execute(exeSQL)
        con.commit()
        con.close()
        
#***************************************************************************#
    def DeletarInformacao(self):
        con = conexao()
        cursor = con.cursor() 
        cursor.execute(f"delete from users where email = '{self.emailUser}'")
        con.commit()
        con.close()
        

#***************************************************************************#
def selecaoTudo():
    con = conexao()
    cursor = con.cursor()
    cursor.execute("select * from users")
    result = cursor.fetchall()
    for row in result:
        print(row[1], ' | ', row[2])
    con.commit()
    con.close()
    

#***************************************************************************#

#                                 Python                                    #

def titulo():
    centro = 'Faisp - Faculdade interativa'
    print('===' * 35)
    print(centro.rjust(60))
    print('===' * 35)
    
#***************************************************************************#
def linha():
    print('---' * 35)

#***************************************************************************#
def tela(opcao):
    print("Aguarde...")
    time.sleep(0.8)
    linha()
    if opcao == '1':
        resposta = 'S'
        nomeC = str(input("Informe o seu Nome Completo: ")).strip().capitalize()
        emailC = input("Digite seu email: ")
        user = Users(nomeC, emailC)
        user.InserirAluno()
        print("Usuario Cadastrado com sucesso")
        resposta = str(input("Quer cadastrar mais (s/n): ")).strip().upper()[0]
        while resposta not in 'SN':
            resposta = str(input("Dados Inválidos. Por favor, informe com (s) ou (n): ")).strip().upper()[0]
            if resposta == 'S':
                tela(opcao)

    if opcao == '2':
        global emailAntigo
        emailAntigo = input("Digite o seu E-mail atual: ")
        linha()
        print("Esse o seu cadastro atual")
        linha()
        user.selecaoEmail()
        mudar = str(input("Gostaria de mudar o seu cadastro? ")).strip().upper()[0]
        if mudar != 'S':
            nomeNovo = str(input("Digite o seu novo nome: "))
            emailNovo = input("Digite o seu novo email: ")
            user = Users(nomeNovo, emailNovo)
            user.AlterarInformacao()
            linha()
            print("Usuario Alterado com sucesso")
            linha()
        else:
            print("erro")
            
            
#***************************************************************************#
opcao = 0
titulo()
while opcao != 6:
    print('''[ 1 ] incluir um Aluno(a).
[ 2 ] Editar Aluno.
[ 3 ] Excluir Aluno.
[ 4 ] Listar E-mail Cadastrado.
[ 5 ] Finaliza o Programa.''')
    linha()
    opcao = input("Qual e a opção: ")
    linha()
    while opcao not in '1' '2' '3' '4' '5' '6':
        opcao = input("Qual e a opção: ")
        linha()
# Opção "1"
    if opcao == '1':
        tela(opcao)
        titulo()
        

      
# Opção "2"
    if opcao == '2':
        tela(opcao)


      
# Opção "3"
    if opcao == '3':
        user = Users("","")
        user.selecaoEmail()
        email = input("Informe o email para deletar: ")
        user = Users("",email)
        if (input("Tem certeza que deseja excluir esse usuário? Essa ação não poderá ser desfeita (s/n): ") == "s"):
            user.DeletarInformacao()
            print("Usuario excluido com sucesso")
        linha()

      
# Opção "4"
    if opcao == '4':
        selecionarPorEmail = input("Informe o seu E-mail: ")
        user = Users("",selecionarPorEmail)
        linha()
        user.selecaoEmail()
        linha()


# Opção "5"
    if opcao == '5':
        print("Processando Todos os Dados")
        time.sleep(2)
        linha()
        print("Todos os cadastrados")
        selecaoTudo()
        linha()
        break
print('Fim do Programa! Obrigado!!')