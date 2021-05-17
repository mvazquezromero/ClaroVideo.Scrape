import requests
import json
import pandas as pd

#Variables
title = [] 
original_title = [] 
years = [] 
duration = [] 
serieormovie = [] 

#Variable Plus Ultra
package = [] #  (Alquiler/Renta , Permanente, Suscripcion) 

#Variable Extra
description = []
rating_code = [] #Clasificación por edades
id_index = []

#EL Api donde se encuentra la lista en formato JSON de las peliculas x genero. 
#Diccionario de las api que vamos a scrapear.
dic_categorias = {
        'accionyAventura' : "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&quantity=50&from=0&level_id=GPS&order_way=ASC&order_id=50&filter_id=39263"
        ,'bibliografica':   "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75889"
        ,'cienciaFiccion' : "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75890"
        ,'cinedeOro' :      "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75891"
        ,'clasicas' :       "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75892"
        ,'comedias' :	    "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75893"
        ,'deportes' :       "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75894"
        ,'drama' :          "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75895"
        ,'documentales' :   "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75896"
        ,'familiares' :     "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75897"
        ,'historicas' :     "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75898"
        ,'infantiles' :     "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75899"
        ,'lartinoAmericanas':"https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75900"
        ,'musica' :         "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75901"
        ,'romanticas' :     "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75902"
        ,'terrorySuspenso': "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75903"

        ,'rn_AccionyAventura':  "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75379"
        ,'rn_Animevideojuego':  "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75948"
        ,'rn_Bibliografica':    "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75380"
        ,'rn_CienciaFiccion':   "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75429"
        ,'rn_Clasicas':         "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75430"
        ,'rn_Comedias':	        "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75949"
        ,'rn_Deportes':         "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75431"
        ,'rn_Drama':            "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=74964"
        ,'rn_Familiares':       "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75433"
        ,'rn_Historicas':       "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75434"
        ,'rn_Infantiles':       "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75658"
        ,'rn_LartinoAmericanas':"https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=74965"
        ,'rn_Musica':           "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75950"
        ,'rn_Romanticas':       "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=74966"
        ,'rn_TerrorySuspenso':  "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75951"
        }



#iteramos los valores del diccionario. 
for categoria in dic_categorias.values() :
    #Cargamos la data en formato JSON de la api
    r = requests.get(categoria)
    data = json.loads(r.text)

    #iteramos para sacar los datos
    for peli in range(len(data['response']['groups'])):
        
        #Index por ID
        id_index.append(data['response']['groups'][peli]["id"].text)
		#Titulo
        try:    #Uso Try y Except para que la aplicacion no se corte ante cualquier dato vacio. 
                #De esta forma no perdemos los datos recolectados
                title.append(data['response']['groups'][peli]["title"].text) 
        except:
                title.append('N/A')

        #Titulo Original
        try:
                original_title.append(data['response']['groups'][peli]["title_original"]).text
        except:
                original_title.append('N/A')

        #Año
        try:
                years.append(data['response']['groups'][peli]["year"].text)
        except:
                years.append('N/A')

        #Duracion
        try:
                duration.append(data['response']['groups'][peli]["duration"].text)
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
                description.append(data['response']['groups'][peli]["description"].text)
        except:
                description.append("N/A")
        
        #Paquete   "susc,briefcase,download"
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
            rating_code.append(data['response']['groups'][peli]["rating_code"].text)
        except:
            rating_code.append("N/A")


##Añadimos los datos en un dataframe:
peliculas = list(zip(title,original_title, years, duration, serieormovie, package, rating_code, description))
columns = ['Titulo','Titulo Original', 'Año', 'Duracion','Tipo', 'Paquete', 'Clasifiacion', 'Descripcion']


df_duplicados = pd.DataFrame(peliculas, columns=columns, index= id_index)      #CREAMOS un DataFrame con Pandas, contenedor de la pelicula y Indexamos x ID

df = df_duplicados.drop_duplicates()      #Eliminamos los duplicados

#write = pd.ExcelWriter('ClaroVideosDefinitivo.xlsx')
#df.to_excel(write)
#write.save()

with open('claro-video.json', "w", encoding="utf-8") as file:
    str((df)).encode('utf-8')
    json.dump((df), file, indent=4, ensure_ascii=False)

#Chequeamos que el codigo corrio por completo
print("La casa esta en orden")













