import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

url = "https://api.github.com/users/"

# poega o input do usuario
user=str(input("Digite o usuario: "))

# manda a request para a url ex: https://api.github.com/users/al0nnso
dados=requests.get(url+user)

# printa o objeto
#print(dados.json()["name"])

# cria um objeto com os dados do seu perfil no github
github={
    "name":dados.json()["name"],
    "uid":dados.json()["id"],
    "descricao":dados.json()["bio"],
    "follows":"{} - {}".format(dados.json()["followers"],dados.json()["following"])
   # "privado":str(dados.json()["private"]),
}

# funcao que carrega os repositorios
def repos(user):
    # manda request para pegar os repositorios
    repositorios= requests.get(url+user+"/repos").json()
    for i in repositorios:
        print(i["name"]+" - "+str(i["stargazers_count"])+" estrelas")
    print(bcolors.ENDC)
    #return repositorios

# printando bonitinho
print(github)
print(bcolors.OKGREEN+"##############################")
print("#### Seus dados do github ####")
print("##############################"+bcolors.OKBLUE)
print("Nome: "+github["name"]+" "+str(github["follows"])+" ("+str(github["uid"])+")")
print(github["descricao"])
print(bcolors.OKGREEN+"### REPOSITORIOS ###"+bcolors.OKCYAN)
repos(user)
