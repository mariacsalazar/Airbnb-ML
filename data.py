import pandas as pd
import os


def read_files():
    dir = os.getcwd()

    csv_files = [file for file in os.listdir(dir) if file.endswith('.csv')]
    dfs = []
    for file in csv_files:
       
        name_parts = file.split('_')
        city = name_parts[0]
        type = name_parts[1].split('.')[0]
        
   
        path = os.path.join(dir, file)
        df = pd.read_csv(path)
        
        
        df['city'] = city
        df['days'] = type
        dfs.append(df)
    df_final = pd.concat(dfs, ignore_index=True)


    return df_final.to_parquet("raw_data.parquet", index=False)


def main():
    read_files()

if __name__ == '__main__':
    main()

