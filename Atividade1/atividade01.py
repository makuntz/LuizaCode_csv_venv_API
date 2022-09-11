import csv


def ler_arquivo_csv():
    arq_csv = open("musicasss.csv", "r")
    conteudo_arquivo = arq_csv
    print(conteudo_arquivo)
    arq_csv.close()
    

def principal():
    """Ler o arquivo csv e transformar em arquivo json"""
    registros = ler_arquivo_csv()
    return registros
    
    

if __name__ == "__main__":
    principal()
    