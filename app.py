import psycopg2
import time


global emailAtual
global nomeAtual
#***************************************************************************#

#                                 Postgresql                                 #
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
    def AlterarInformacao(self, emailAtual):
        con = conexao()
        cursor = con.cursor()
        exeSQL = "update users set "
        if (self.nomeUser != '' or self.nomeUser == self.nomeUser):
            exeSQL += f"nome = '{self.nomeUser}', "
        if (self.emailUser != '' or self.emailUser == self.emailUser):
            exeSQL += f"email = '{self.emailUser}' "
        exeSQL = exeSQL[:-2]
        exeSQL += f"' WHERE email = '{emailAtual}'"
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


def nomeA(n, e):
    con = conexao()
    cursor = con.cursor()
    exeSQL = f"select nome, email from users where nome = '{n}' and email = '{e}'"
    cursor.execute(exeSQL)
    result = cursor.fetchall()
    try:
        if f"{e}" in result[0]:
            print("Esse o seu cadastro atual")
            linha()
            for row in result:
                print(row[0], ' | ', row[1])
    except:
            linha()
            print("O usuario não está cadastrado. Por favor cadastra-se")
            linha()
        
    con.commit()
    con.close
 

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
        emailC = input("Digite seu email: ").strip()
        if len(nomeC) > 2 and len(emailC) > 2 and "@" in emailC:
            user = Users(nomeC, emailC)
            user.InserirAluno()
            print("Aguarde...")
            time.sleep(2)
            linha()
            print("Usuario Cadastrado com sucesso\n")
        else:
            linha()
            time.sleep(1)
            print("Suas credencial estão erradas, por favor verifique seu Nome ou E-mail!!\n")
            

    if opcao == '2':
        emailAtual = input("Digite o seu E-mail atual: ")
        nomeAtual = str(input("Digite o seu Nome atual: "))
        ver = nomeA(nomeAtual, emailAtual)
        mudar = str(input("Gostaria de mudar o seu cadastro (s/n)? ")).strip().upper()[0]
        while mudar not in 'SN':
            mudar = str(input('Dados Inválidos. Por favor, informe com S ou N: ')).strip().upper()[0]
        if mudar == 'S':
            print('Fazendo Login')
            print('Aguarde...')
            time.sleep(2)
            linha()
            print('''
[ 1 ] Para trocar o Usuário e senha.
[ 2 ] Para trocar Usuário.
[ 3 ] Para trocar Senha.
[ 4 ] Sair.
                ''')
            op = int(input('Qual e a Opçâo: '))
            print('Processando ...')
            time.sleep(0.6)
            if op == 1:
                emailAtual = input("Digite o seu E-mail para identificá-lo: ")
                nomeNovo = str(input("Digite o seu novo nome: "))
                emailNovo = input("Digite o seu novo email: ")
                user = Users(nomeNovo, emailNovo)
                user.AlterarInformacao(emailAtual)
                linha()
                print("Usuario Alterado com sucesso")
                linha()
                
            elif op == 2:
                emailAtual = input("Digite o seu E-mail para identificá-lo: ")
                nomeNovo = str(input("Digite o seu novo nome: "))
                user = Users(nomeNovo, emailAtual)
                user.AlterarInformacao(emailAtual)
                linha()
                print("Nome Alterado com sucesso")
                linha()
                
            elif op == 3:
                emailAtual = input("Digite o seu E-mail para identificá-lo: ")
                emailNovo = str(input("Digite o seu novo email: "))
                user = Users(nomeAtual, emailNovo)
                user.AlterarInformacao(emailAtual)
                linha()
                print("E-mail Alterado com sucesso")
                linha()
            
            elif op == 4:
                linha()
                print("Certo, Obrigado!!")
            
            elif op != 1 or op != 2 or op != 3 or op != 4:
                linha()
                print("Essa opção não existe, por favor informe corretamente")
                linha()
        else:
            linha()
            print("Certo, Obrigado!!")
            linha()
            
            
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
        opcao = input("Por favor digite corretamente: ")
        linha()
    # Opção "1"
    if opcao == '1':
        tela(opcao)
        titulo()
        

    
# Opção "2"
    elif opcao == '2':
        tela(opcao)


    
# Opção "3"
    elif opcao == '3':
        user = Users("","")
        user.selecaoEmail()
        email = input("Informe o email para deletar: ")
        user = Users("",email)
        if (input("Tem certeza que deseja excluir esse usuário? Essa ação não poderá ser desfeita (s/n): ") == "s"):
            user.DeletarInformacao()
            linha()
            print("Usuario excluido com sucesso")
        else:
            linha()
            print("Não há nada para excluir")
        linha()

    
# Opção "4"
    elif opcao == '4':
        selecionarPorEmail = input("Informe o seu E-mail: ")
        user = Users("",selecionarPorEmail)
        linha()
        user.selecaoEmail()
        linha()


# Opção "5"
    elif opcao == '5':
        print("Processando Todos os Dados")
        time.sleep(2)
        linha()
        print("Todos os cadastrados")
        linha()
        selecaoTudo()
        linha()
        break
print('Fim do Programa! Obrigado!!')
print("")