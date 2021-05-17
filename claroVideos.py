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

diccionario_generos = {
                        'Accion y Aventura' : 39263,
                        'Bibliograficas' : 75889,
                        'Ciencia Ficcion' : 75890,
                        'Cine de Oro' : 75891,
                        'Clasicas' : 75892,
                        'Comedias' : 75893,
                        'Deportes' : 75894,
                        'Drama' : 75895,
                        'Documentales' : 75896,
                        'Familiares' : 75897,
                        'Historicas' : 75898,
                        'Infantiles' : 75899,
                        'Latino Americanas' : 75900,
                        'Musica' : 75901,
                        'Romanticas' : 75902,
                        'Terror y Suspenso' : 75903,
                        
}

#Encontramos el api donde se encuentra la lista en formato JSON de las peliculas x genero. 

accionyAventura = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&quantity=50&from=0&level_id=GPS&order_way=ASC&order_id=50&filter_id=39263"
bibliografica = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75889"
cienciaFiccion = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75890"
cinedeOro = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75891"
clasicas = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75892"
comedias  =	"https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75893"
deportes = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75894"
drama = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75895"
documentales = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75896"
familiares = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75897"
historicas = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75898"
infantiles = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75899"
lartinoAmericanas = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75900"
musica = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75901"
romanticas = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75902"
terrorySuspenso = "https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Opera&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=8ncr005l9uepvbc2g2mvjvph96&order_id=200&order_way=DESC&level_id=GPS&from=0&quantity=10000&node_id=75903"

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
            rating_code.append(data['response']['groups'][peli]["rating_code"])
        except:
            rating_code.append("N/A")

    #Añadimos los datos en un dataframe:

    peliculas = list(zip(title,original_title, years, duration, serieormovie, package, rating_code, description))
    columns = ['Titulo','Titulo Original', 'Año', 'Duracion','Tipo', 'Paquete', 'Clasifiacion', 'Descripcion']

    df = pd.DataFrame(peliculas, columns=columns, index= id_index) #modificar
    
    write = pd.ExcelWriter('terrorySuspenso.xlsx')
    df.to_excel(write)
    write.save()
    print('DataFrame guardado con formato xlsx')

all_datos(terrorySuspenso)

print("Pochoclos listos")













