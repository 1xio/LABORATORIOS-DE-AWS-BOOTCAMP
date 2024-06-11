import json
import pandas as pd
from linkedin_api import Linkedin
import html


# Lista de usuarios de interes
usuarios = ['robertolanda395']
perfiles = []

api = Linkedin('xio2003uru@gmail.com', 'linkedin3245')

for usuario in usuarios:
    try:
        perfil = api.get_profile(usuario)
        perfiles.append(perfil)
    except Exception as e:
        print(f"No se logró obtener info de {usuario}: {e}")

# FORMATO LEGIBLE PARA JSON
# Convertir la lista de perfiles a JSON
perfiles_json = json.dumps(perfiles, indent=4)

# Decodificar secuencias de escape Unicode en el JSON
perfiles_json_decodificado = perfiles_json.encode().decode('unicode-escape')

# Cargar los datos en un DataFrame de Pandas
df = pd.read_json(perfiles_json_decodificado)

# Eliminar columnas 
columns_to_drop = ['lastName','geoCountryName','firstName','honors', 'urn_id', 'geoCountryUrn', 'geoLocationBackfilled', 'entityUrn', 'publications', 'elt', 'industryUrn', 'geoLocation', 'displayPictureUrl', 'img_400_400', 'img_200_200', 'img_800_800', 'img_100_100', 'profile_id', 'profile_urn', 'member_urn', 'public_id', 'languages', 'volunteer']

for column in columns_to_drop:
    if column in df.columns:
        df = df.drop(columns=column)
    else:
        print(f"La columna {column} no está presente en el DataFrame.")

# Mostrar el DataFrame después de eliminar las columnas
print(df)

# Guardar los datos procesados en un nuevo archivo CSV en la misma ruta del code
df.to_csv('df_base.csv', index=False)

