import pandas as pd
import os


def read_files():
    directorio = os.getcwd()

    csv_files = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.csv')]
    dfs = []
    for file in csv_files:
       
        name_parts = file.split('_')
        ciudad = name_parts[0]
        tipo = name_parts[1].split('.')[0]  # Eliminar la extensión (.csv)
        
        # Leer el archivo CSV
        path = os.path.join(directorio, file)
        df = pd.read_csv(path)
        
        # Agregar dos columnas con la ciudad y el tipo
        df['city'] = ciudad
        df['days'] = tipo
        dfs.append(df)
    df_final = pd.concat(dfs, ignore_index=True)


    return df_final.to_parquet("raw_data.parquet", index=False)
