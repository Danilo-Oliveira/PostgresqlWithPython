# Dependencias 
# pip3 install psycopg2
# pip3 install pandas   
# pip3 install tabulate
# pip3 install validate-email

import psycopg2
import time
import re
import pandas as pd
from validate_email import validate_email

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
def createTable():
    con = conexao()
    cursor = con.cursor()
    cursor.execute("create table users (id serial primary key, nome varchar(50), email varchar(50))")
    con.commit()
    con.close() 
 
        
#***************************************************************************#
def InserirAluno(novoUser, novoEmail):
    con = conexao()
    cursor = con.cursor()
    cursor.execute(f"insert into users (nome, email) values ('{novoUser}', '{novoEmail}')")
    con.commit()
    con.close()   


#***************************************************************************#
def AlterarEmail(emailNovo, emailAtual):
    con = conexao()
    cursor = con.cursor()
    exeSQL = "update users set "
    if (emailNovo != ''):
        exeSQL += f"email = '{emailNovo}' "
    exeSQL = exeSQL[:-2]
    exeSQL += f"' WHERE email = '{emailAtual}'"
    cursor.execute(exeSQL)
    con.commit()
    con.close()
    
  
#***************************************************************************#
def deleteUser(excluirUser):
    con = conexao()
    cursor = con.cursor() 
    cursor.execute(f"delete from users where email = '{excluirUser}'")
    con.commit()
    con.close()
        

#***************************************************************************#
def selecaoTudo():
    column_names = ["Nome do Usuário", "E-mail"]
    con = conexao()
    cursor = con.cursor()
    cursor.execute("select nome, email from users")
    result = cursor.fetchall()
    con.commit()
    con.close()
    
    df = pd.DataFrame(result, columns=column_names)
    df.set_index('Nome do Usuário', inplace=True)
    return print(df.to_markdown())


#***************************************************************************#
def verifcadorUser(nomeVerificado, emailVerificado):
    column_names = ["Nome do Usuário", "E-mail"]
    con = conexao()
    cursor = con.cursor()
    exeSQL = f"select nome, email from users where nome = '{nomeVerificado}' and email = '{emailVerificado}'"
    cursor.execute(exeSQL)
    result = cursor.fetchall()
    result.append("")

    if f"{emailVerificado}" in result[0]:
        print("\033[36mEsse o seu cadastro atual\033[m\n")
        df = pd.DataFrame(result, columns=column_names)
        df.set_index('Nome do Usuário', inplace=True)
        print(df.to_markdown())
            
        return True
   
    else:
        print("\033[31mO usuario não está cadastrado. Por favor cadastra-se\033[m")
        return False
 
    con.commit()
    con.close

#***************************************************************************#
def verifcadorEmail(e):
    column_names = ["Nome do Usuário", "E-mail"]
    con = conexao()
    cursor = con.cursor()
    exeSQL = f"select nome, email from users where email = '{e}'"
    cursor.execute(exeSQL)
    result = cursor.fetchall()
    result.append("")

    if f"{e}" in result[0]:
        print("\033[36mEsse o seu cadastro atual\033[m\n")
        df = pd.DataFrame(result, columns=column_names)
        df.set_index('Nome do Usuário', inplace=True)
        print(df.to_markdown())
            
        return True
   
    else:
        print("\033[31mO usuario não está cadastrado. Por favor cadastra-se\033[m")
        
        return False
        
    con.commit()
    con.close
    
    
#***************************************************************************#
def validadorNomeEmail(validadorNome, validadorEmail): 

    regex_name = re.compile(r'^([A-Za-z]+)( [A-Za-z]+)*( [A-Za-z]+)*$', 
            re.IGNORECASE) 

    res = regex_name.search(validadorNome)
    
    validandoEmail = validate_email(validadorEmail)
    
    if validandoEmail == True: 
        return validandoEmail

    else: 
        print("\033[31mInvalid Email\033[m")
        return False
 
    if res:
        return True
  
    else:
        print("\033[31mSeu nome está inválido\033[m")
        return False
 


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
    print("\033[36mAguarde...\033[m")
    time.sleep(0.8)
    linha()
    if opcao == '1':
        resposta = 'S'
        nomeC = str(input("\033[33mInforme o seu Nome Completo\033[m: ")).strip().capitalize()
        emailC = input("\033[33mDigite seu email\033[m: ").strip()
        validador = validadorNomeEmail(nomeC, emailC)
        if len(nomeC) > 2 and len(emailC) > 2 and validador == True:
            #user = Users(nomeC, emailC)
            newUser = InserirAluno(nomeC, emailC)
            print("\033[36mAguarde...\033[m")
            time.sleep(2)
            linha()
            print("\033[32mUsuario Cadastrado com sucesso\033[m\n")
        else:
            linha()
            time.sleep(1)
            print("\033[31mSuas credencial estão erradas, por favor verifique seu Nome ou E-mail!!\033[m\n")
            

    if opcao == '2':
        emailAtual = input("\033[33mDigite o seu E-mail atual\033[m: ").strip()
        nomeAtual = str(input("\033[33mDigite o seu Nome atual\033[m: ")).strip().capitalize()
        ver = verifcadorUser(nomeAtual, emailAtual)
        linha()
        if ver == True:
            mudar = str(input("\033[36mGostaria de mudar o seu cadastro (s/n)?\033[m ")).strip().upper()[0]
            while mudar not in 'SN':
                mudar = str(input('\033[31mDados Inválidos. Por favor, informe com S ou N\033[m: ')).strip().upper()[0]
            if mudar == 'S' and ver == True:
                    
                print('\033[36mFazendo Login\033[m')
                print('\033[36mAguarde...\033[m')
                time.sleep(2)
                linha()
                print('''
    [ 1 ] Para trocar o Usuário e senha.
    [ 2 ] Para trocar Usuário.
    [ 3 ] Para trocar Email.
    [ 4 ] Sair.
                    ''')
                op = int(input('\033[36mQual e a Opçâo\033[m: '))
                print('\033[36mProcessando ...\033[m')
                time.sleep(0.6)
                
                if op == 1:
                    emailAtual = input("\033[33mDigite o seu E-mail para identificá-lo\033[m: ").strip()
                    nomeNovo = str(input("\033[33mDigite o seu novo nome\033[m: ")).strip().capitalize()
                    emailNovo = input("\033[33mDigite o seu novo email\033[m: ").strip()
                    validador = validadorNomeEmail(nomeNovo, emailNovo)
                    if len(nomeNovo) > 2 and len(emailNovo) > 2 and validador == True:
                        user = Users(nomeNovo, emailNovo)
                        user.AlterarInformacao(emailAtual)
                        linha()
                        print("\033[32mUsuario Alterado com sucesso\033[m")
                        linha()
                    else:
                        linha()
                        time.sleep(1)
                        print("\033[31mSuas credencial estão erradas, por favor verifique seu Nome ou E-mail!!\033[m\n")
                            
                elif op == 2:
                    emailAtual = input("\033[33mDigite o seu E-mail para identificá-lo\033[m: ").strip()
                    nomeNovo = str(input("\033[33mDigite o seu novo nome\033[m: ")).strip().capitalize()
                    validador = validadorNomeEmail(nomeNovo, emailAtual)
                    if len(nomeNovo) > 2 and len(emailAtual) > 2 and validador == True:
                        user = Users(nomeNovo, emailAtual)
                        user.AlterarInformacao(emailAtual)
                        linha()
                        print("\033[32mNome Alterado com sucesso\033[m")
                        linha()
                    else:
                        linha()
                        time.sleep(1)
                        print("\033[31mSuas credencial estão erradas, por favor verifique seu Nome ou E-mail!!\033[m\n")
                        
                elif op == 3:
                    emailAtual = input("\033[33mDigite o seu E-mail para identificá-lo\033[m: ").strip()
                    emailNovo = str(input("\033[33mDigite o seu novo email\033[m: ")).strip()
                    validador = validadorNomeEmail(emailNovo, emailAtual)
                    if len(emailNovo) > 2 and len(emailAtual) > 2 and validador == True:
                        AlterarEmail(emailNovo, emailAtual)
                        linha()
                        print("\033[32mE-mail Alterado com sucesso\033[m")
                        linha()
                    else:
                        linha()
                        time.sleep(1)
                        print("\033[31mSuas credencial estão erradas, por favor verifique seu Nome ou E-mail!!\033[m\n")
                elif op == 4:
                    linha()
                    print("\033[32mCerto, Obrigado!!\033[m")
                    linha()
                
                elif op != 1 or op != 2 or op != 3 or op != 4:
                    linha()
                    print("\033[31mEssa opção não existe, por favor informe corretamente\033[m")
                    linha()
            else:
                linha()
                print("\033[32mCerto, Obrigado!!\033[m")
                linha()
            
            
#***************************************************************************#
opcao = 0
try:
    createTable()
    print('\033[32mCriamos uma tabela com o Nome "Users" e as colunas!!\n\033[m')
    selecaoTudo()
    print("")
except psycopg2.errors.DuplicateTable:
    pass
    
titulo()

while opcao != 6:
    print('''
[ 1 ] incluir um Aluno(a).
[ 2 ] Editar Aluno.
[ 3 ] Excluir Aluno.
[ 4 ] Listar E-mail Cadastrado.
[ 5 ] Finaliza o Programa.''')
    linha()
    opcao = input("\033[36mQual e a opção\033[m: ")
    linha()
    while opcao not in '1' '2' '3' '4' '5' '6':
        opcao = input("\033[31mPor favor digite corretamente: ")
        linha()
    try:
        # Opção "1"
        if opcao == '1':
            tela(opcao)
            titulo()

        
    # Opção "2"
        elif opcao == '2':
            tela(opcao)


        
    # Opção "3"
        elif opcao == '3':
            emailExcluir = input("\033[33mDigite o seu E-mail atual\033[m: ").strip()
            linha()
            verificador = verifcadorEmail(emailExcluir)
            #userExcluir = deleteUser(emailExcluir)
            if verificador == True:
                linha()
                res = str(input("\033[31mTem certeza que deseja excluir esse usuário? Essa ação não poderá ser desfeita (s/n)\033[m: ")).strip().upper()[0]
                while res not in 'SN':
                    res = str(input('\033[31mDados Inválidos. Por favor, informe com S ou N\033[m: ')).strip().upper()[0]
                if res == 'S':
                    linha()
                    excluirUser = deleteUser(emailExcluir)
                    print("\033[36mProcessando Todos os Dados\n\033[m")
                    time.sleep(2)
                    print("\033[32mUsuario excluido com sucesso\033[m")
                else:
                    linha()
                    print("\033[32mCerto, Obrigado\033[m")
            elif verificador == False:
                linha()
                print("\033[31mNão há nada para excluir\033[m")
            linha()

        
    # Opção "4"
        elif opcao == '4':
            selecionarPorEmail = input("\033[33mInforme o seu E-mail\033[m: ").strip()
            print("\033[36mProcessando Todos os Dados\033[m")
            time.sleep(2)
            user = verifcadorEmail(selecionarPorEmail)
            print("")
    # Opção "5"
        elif opcao == '5':
            print("\033[36mProcessando Todos os Dados\033[m")
            time.sleep(2)
            linha()
            print("\033[36mTodos os cadastrados\033[m")
            linha()
            selecaoTudo()
            linha()
            break
    except ValueError:
        print("\033[31mDigite corretamente\033[m")
        linha()
    
    except KeyboardInterrupt:
        print("\033[31mDigite corretamente\033[m")
        linha()

print('\033[35mFim do Programa! Obrigado!!\033[m')