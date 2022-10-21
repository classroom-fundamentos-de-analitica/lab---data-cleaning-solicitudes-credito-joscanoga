"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    #leer datos
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    #borar filas con valores faltantes
    df.dropna(inplace=True)
    #sexo
    df["sexo"] = df["sexo"].apply(lambda x: str(x).lower().strip())
    # tipo_de_emprendimiento
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].apply(lambda x: str(x).lower().strip())
    # idea_negocio
    df["idea_negocio"] = df["idea_negocio"].apply(lambda x: str(x).lower().replace("-", " ").replace("_", " ").strip())
    # barrio
    df["barrio"] = df["barrio"].apply(lambda x: str(x).lower().replace("_"," ").replace("-"," "))##revisar
    #estrato no necesita cambios
    #comuna no nececita cambios
    # fecha_de_beneficio
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"],dayfirst=True)
    # monto del credito
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x: str(x).strip("$").strip().replace(",", "").replace(".00", ""))
    # print((len(df["monto_del_credito"].unique())))
    # línea_credito
    df["línea_credito"] = df["línea_credito"].apply(lambda x: str(x).lower().replace("-", " ").replace("_", " ").strip())
    #print("linea credito",(len(df["línea_credito"].unique())))
    #eliminar duplicados y faltantes
    df.drop(['Unnamed: 0'], axis=1,inplace=True)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)


    return df
clean_data()