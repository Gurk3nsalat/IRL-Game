import pandas as pd


ASSETS_PATH = "./assets/"

if __name__ == '__main__':
    df = pd.read_excel(ASSETS_PATH + "PyXl.xlsx",sheet_name="Sheet1")

    df.at[6,"Test"] = 1000

    print(df)

    for row in df.iterrows():
        print(row)



    df.to_excel(ASSETS_PATH + "PyXl.xlsx",index = False)
