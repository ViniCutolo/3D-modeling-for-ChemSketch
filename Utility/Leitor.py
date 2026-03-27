from tkinter import Tk, filedialog

def caminho():
    #Vamos achar o caminho do arquivo
    root = Tk()
    #bora esconder janelinha feia
    root.withdraw()

    #vamos pedir para ele abrir o arquivo
    caminho = filedialog.askopenfilename(
            title="Selecione o arquivo da molécula",
            filetypes=[
                ("Arquivos Mol", "*.mol")
            ]
    )
    return caminho

def traducao(path):
    # Abrindo o arquivo no modo de leitura
    arquivo = open(path, 'r')

    # Lendo todo o conteúdo do arquivo
    conteudo = arquivo.read()
    conteudo=conteudo.split() #como é uma string unica, quero separar-lo
    #if __name__=='__main__':
     # print(conteudo)

    # Fechando o arquivo
    arquivo.close()
    return conteudo

def organiza(texto):
    # esse vai ser o nosso dicionario fodastico
    # 
    info={
        "nome" : "",
        "q.atomos" : 0,
        "q.ligações" : 0
        }
    # essa variavel vai guardar onde estamos na string, para fazermos em blocos
    local=0
    # Em qual linha estamos 
    etapa=0
    # quando eu for anotar os atomos, eu preciso guardar em qual atomo estou
    etapa2=1
    while True:
       #criando o dicionario
       if texto[local]=="M":
            break
       local, etapa, info, etapa2= dicionario(local,etapa, texto, info, etapa2)
    
    if __name__=='__main__':
        print(info)
    return info

def dicionario(local, etapa, texto, dici, etapa2):
    # dici é uma abreviação para dicionario. Perdão a confusão

    # quais entradas que não me interessam dentro do texto
    proibido=["0","V2000"]
    while True:
        #vamos criar uma string para
        string=texto[local]
        if string in proibido:
            local+=1
            continue
        elif etapa==3:
            # vamos fazer uma brincadeirinho
            # nome vai ser a entrada do atomo
            nome = "atomo "+str(etapa2)
        elif etapa==4:
            # mais uma brincadeirinha galera :3
            # nome vai ser a entrada da ligação
            nome= "ligação "+str(etapa2)

        break
    #vamos usar o etapa para garantir que vamos adicionar no local correto
    if etapa==0:
        dici["nome"]=string
        etapa+=1
        local+=1
    elif etapa==1:
        dici["q.atomos"]=int(string)
        etapa+=1
        local+=1
    elif etapa==2:
        dici["q.ligações"]=int(string)
        etapa+=1
        local=13
    elif etapa==3:
        # essa parte nos diz a posição espacial de cada atomo e qual atomo é
        dici[nome]=[texto[local],texto[local+1],texto[local+2],texto[local+3]]
        local+=12
        if etapa2+1>dici["q.atomos"]:
            etapa+=1
            etapa2=1
        else:
            etapa2+=1
    elif etapa==4:
        # essa parte nos diz quais atomos estão fazendo ligações
        dici[nome]=[texto[local],texto[local+1],texto[local+2]]
        local+=6
        if etapa2+1>dici["q.ligações"]:
            etapa+=1
        else:
            etapa2+=1
    return local, etapa, dici, etapa2

if __name__=='__main__':
    # Saca só o script do Viniboy B)
    path = caminho()
    texto=traducao(path)
    organiza(texto)
