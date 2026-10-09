import pandas as pd
from pathlib import Path

pasta_home = ...

def converter_csv():
    pasta_home = input("Digite o local dos arquivos txt: ")
    pasta_home = Path(pasta_home)
    saida = pasta_home.parent / "csvs"
    saida.mkdir(exist_ok = True)

    arquivo_txttocsv = sorted(pasta_home.glob("*.txt"))

    if not arquivo_txttocsv:
        raise SystemExit("Nenhum TXT foi encontrado")

    erros = []
    
    for arquivo in arquivo_txttocsv:
        try:
            df = pd.read_csv(arquivo, sep="|")
            df.to_csv(saida / f"{arquivo.stem}.csv", index=False)
        except Exception as e:
            erros.append((arquivo.name, str(e)))

    print(f"{len(arquivo_txttocsv) - len(erros)} de {len(arquivo_txttocsv)} arquivos convertidos") 

def concatenar_csv():
    pasta_home = input("Digite o local dos arquivos csv: ")
    pasta_home = Path(pasta_home)
    arquivos_concatenar = sorted(pasta_home.glob("*.csv"))

    if not arquivos_concatenar:
        raise SystemExit("Nenhum CSV foi encontrado")

    print(f"{len(arquivos_concatenar)} arquivos encontrados")
    
    final = pd.concat((pd.read_csv(a) for a in arquivos_concatenar), ignore_index=True)
    final.to_csv(pasta_home.parent / "csv_unido.csv", index=False)
    
    print(f"Total de linhas: {len(final)}")


print("_______________ | conversor e concatenador | _______________")

opc = input("\n[1] Converter TXT to CSV\n[2] Concatenar diferentes arquivos CSV\n\nDigite:")

opc= int(opc)

if opc == 1:
    converter_csv()
    
    opc = input("Deseja concatenar os CSV em um unico arquivo [S]im | [N]ão: ").islower()
    
    if opc == "s":
        concatenar_csv()
    else:
        raise SystemExit("Saindo")
        
elif opc == 2:
    concatenar_csv()
else:
    print("Nada valido")
    raise SystemExit("Saindo")




