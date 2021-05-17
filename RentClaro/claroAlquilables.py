import requests
import json
import pandas as pd

#Variables
title = [] 
original_title = [] 
years = [] 
duration = [] 
serieormovie = [] 
package = [] #  (Alquiler/Renta , Permanente, Suscripcion) 
description = [] 
rating_code = [] #Clasificación por edades 
id_index = []

#Encontramos el api donde se encuentra la lista en formato JSON de las peliculas x genero. 

rn_AccionyAventura =    "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75379"
rn_Animevideojuego =    "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75948"
rn_Bibliografica =      "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75380"
rn_CienciaFiccion =     "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75429"
rn_Clasicas =           "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75430"
rn_Comedias  =	        "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75949"
rn_Deportes =           "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75431"
rn_Drama =              "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=74964"
rn_Familiares =         "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75433"
rn_Historicas =         "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75434"
rn_Infantiles =         "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75658"
rn_LartinoAmericanas =  "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=74965"
rn_Musica =             "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75950"
rn_Romanticas =         "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=74966"
rn_TerrorySuspenso =    "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75951"


#iterar
def all_datos(api_genero):

    #Cargamos la data en formato JSON.
    r = requests.get(api_genero)
    data = json.loads(r.text)
	
	#iteramos para sacar toda la info.
    for peli in range(len(data['response']['groups'])):

        #Index por ID
        id_index.append(data['response']['groups'][peli]["id"])            
		#Titulo
        try:
                title.append(data['response']['groups'][peli]["title"])
        except:
                title.append('N/A')

        #Titulo Original
        try:
                original_title.append(data['response']['groups'][peli]["title_original"])
        except:
                original_title.append('N/A')

        #Año
        try:
                years.append(data['response']['groups'][peli]["year"])
        except:
                years.append('N/A')

        #Duracion
        try:
                duration.append(data['response']['groups'][peli]["duration"])
        except:
                duration.append("N/A")
        
        #Type
        try:
            if data['response']['groups'][peli]["is_series"] == True:
                serieormovie.append("Serie")
            else:
                serieormovie.append("Pelicula")
        except:
                serieormovie.append("N/A")
        
        #Descripcion
        try:
                description.append(data['response']['groups'][peli]["description"])
        except:
                description.append("N/A")
        
        #Paquete
        try:
            if data['response']['groups'][peli]["format_types"] == "susc":
                package.append("Suscripcion")
            elif data['response']['groups'][peli]["format_types"] == "ppe,download":
                package.append("Alquiler 48hs")
            elif data['response']['groups'][peli]["format_types"] == "ppe":
                package.append("Alquiler 24hs")
            elif data['response']['groups'][peli]["format_types"] == "free,download":
                package.append("Free, Download")
            elif data['response']['groups'][peli]["format_types"] == "susc,briefcase,download":
                package.append("Briefcase, Download, Suscripcion")
            else:
                package.append("N/A")
        except:
                package.append("N/A")
        
        #Clasificación por edades
        try:
            rating_code.append(data['response']['groups'][peli]["rating_code"])
        except:
            rating_code.append("N/A")


    #Añadimos los datos en un dataframe:

    peliculas = list(zip(title,original_title, years, duration, serieormovie, package, rating_code, description))
    columns = ['Titulo','Titulo Original', 'Año', 'Duracion','Tipo', 'Paquete', 'Clasifiacion', 'Descripcion']

    df = pd.DataFrame(peliculas, columns=columns, index=id_index) #modificar
    
    write = pd.ExcelWriter('rn_TerrorySuspenso.xlsx')
    df.to_excel(write)
    write.save()
    print('DataFrame guardado con formato xlsx')

all_datos(rn_TerrorySuspenso)

print("Pochoclos listos")












