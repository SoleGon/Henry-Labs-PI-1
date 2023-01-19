## Importo las librerias que necesito para trabajar

from fastapi import FastAPI
import pandas as pd


## Instancio mi Appi

app = FastAPI(title='Labs-Proyecto1',
            description='Henry-Data 06',
            version= '1.0.1'
            )

## Funcion para que la Api tome mi Dataframe para hacer las consultas 

@app.get('/')
async def read_root():
    return {'Appi de Mariana Soledad Gonzalez'}
    
@app.on_event('startup')
async def startup():
    global data
    data = pd.read_csv('peliculasyseries.csv') 


## Funcion para el servidor

@app.get('/')
async def index():
    return {'Bienvenidos a Mi Appi'}

@app.get('/about/')
async def about():
    return {'Labs-Proyecto1: Data 06'}



# Primera consulta: Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
# Prueba Ejemplo: get_word_count(netflix,love)

@app.get('/get_word_count/({plataforma}, {palabra})')
async def get_word_count( palabra:str,nombre_plataforma: str):## los parametros son la plataforma y la palabra
   if nombre_plataforma== 'netflix': ## si la plataforma es netflix
        nombre=data[data['id'].str.startswith('n')] #Aca veo la plataforma indicada
        titulo=nombre[nombre['title'].str.contains(str(palabra),case=False)] #titulo indicado 
        conteo=titulo['id'].count()# cuento los id para saber la cantidad
        final= {'Plataforma': [str(nombre_plataforma)], 'Cantidad': [int(conteo)]}# tengo mi rdo final
        return final


   elif nombre_plataforma== 'amazon':## si la plataforma es amazon
        nombre=data[data['id'].str.startswith('a')] #Aca veo la plataforma indicada
        titulo=nombre[nombre['title'].str.contains(str(palabra),case=False)] #titulo indicado,                                                        
        conteo=titulo['id'].count()# cuento los id para saber la cantidad
        final= {'Plataforma': [str(nombre_plataforma)], 'Cantidad': [int(conteo)]}# tengo mi rdo final
        return final


   elif  nombre_plataforma== 'hulu':## si la plataforma es hulu
        nombre=data[data['id'].str.startswith('h')] #Aca veo la plataforma indicada
        titulo=nombre[nombre['title'].str.contains(str(palabra),case=False)] #titulo indicado, 
        conteo=titulo['id'].count()# cuento los id para saber la cantidad
        final= {'Plataforma': [str(palabra)], 'Cantidad': [int(conteo)]}# tengo mi rdo final
        return final

   elif nombre_plataforma== 'disney':## si la plataforma es disney
        nombre=data[data['id'].str.startswith('d')] #Aca veo la plataforma indicada
        titulo=nombre[nombre['title'].str.contains(str(palabra),case=False)] #titulo indicado, 
        conteo=titulo['id'].count()# cuento los id para saber la cantidad
        final= {'Plataforma': [str(nombre_plataforma)], 'Cantidad': [int(conteo)]}# tengo mi rdo final
        return final
   else :
        return('Verifique los valores ingresados ') 



# Segunda Consulta: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
# Resultado Ejemplo= get_score_count(netflix,85,2010)

@app.get('/get_score_count/( {plataforma},{score} {Anio})')
async def get_score_count( Anio: int,score_ingresado:str,plataforma: str):## los parametros son la plataforma, score y anio

    if plataforma == 'netflix':## si es netflix
        pelis=data[data['type']=='movie'] #Filtro de peliculas
        nombre=pelis[pelis['id'].str.startswith('n')] #Filtro de plataforma
        scores=nombre[nombre['score'] > int(score_ingresado)] #Filtro de Puntaje
        a=scores[scores['release_year'] == int(Anio)] #Filtro de Año
        cont=a['id'].count() # cuento los id para tener mi rdo
        df2 = {'Plataforma': [str(plataforma)], 'Cantidad': [int(cont)]}
        return df2


    elif plataforma == 'disney':## si es disney
        pelis=data[data['type']=='movie'] #Filtro de peliculas
        nombre=pelis[pelis['id'].str.startswith('d')] #Filtro de plataforma
        scores=nombre[nombre['score'] > int(score_ingresado)] #Filtro de Puntaje
        a=scores[scores['release_year'] == int(Anio)] #Filtro de Año
        cont=a['id'].count()## cuento los id para tener mi rdo
        df2 = {'Plataforma': [str(plataforma)], 'Cantidad': [int(cont)]}
        return df2


    elif plataforma == 'hulu':## si es hulu
        pelis=data[data['type']=='movie'] #Filtro de peliculas
        nombre=pelis[pelis['id'].str.startswith('h')] #Filtro de plataforma
        scores=nombre[nombre['score'] > int(score_ingresado)] #Filtro de Puntaje
        a=scores[scores['release_year'] == int(Anio)] #Filtro de Año
        cont=a['id'].count()## cuento los id para tener mi rdo
        df2 = {'Plataforma': [str(plataforma)], 'Cantidad': [int(cont)]}
        return df2



    elif plataforma == 'amazon':## si la plataforma es amazon
        pelis=data[data['type']=='movie'] #Filtro de peliculas
        nombre=pelis[pelis['id'].str.startswith('a')] #Filtro de plataforma
        scores=nombre[nombre['score'] > int(score_ingresado)] #Filtro de Puntaje
        a=scores[scores['release_year'] == int(Anio)] #Filtro de Año
        cont=a['id'].count()## cuento los id para tener mi rdo
        df2 = {'Plataforma': [str(plataforma)], 'Cantidad': [int(cont)]}
        return df2
    else:
        return('Verfique los valores ingresados')

## Tercer Consulta: La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos
#Prueba : get_second_score('amazon')


@app.get('/get_second_score/({plataforma})')
async def get_second_score( nombre_plataforma: str):## el parametro es la plataforma

    if  nombre_plataforma== 'amazon':## si es amazon
        movies=data[data['type']=='movie'] #Aca veo las peliculas
        plat=movies[movies['id'].str.startswith('a')] #aAca veo la plataforma indicada
        orden=plat.sort_values(by=['score', 'title'],ascending=[False, True])# Aca Ordeno segun lo solicitado  
        final =  orden.title.iloc[1]## aca me quedo con la segunda posicion
        rdo = {'La segunda pelicula es': [str(final)]}
        return rdo

    elif nombre_plataforma == 'netflix':## si es netflix
        movies=data[data['type']=='movie'] #Aca veo las peliculas
        plat=movies[movies['id'].str.startswith('n')] #aAca veo la plataforma indicada
        orden=plat.sort_values(by=['score', 'title'],ascending=[False, True])# Aca Ordeno segun lo solicitado    
        final =  orden.title.iloc[1]## aca me quedo con la segunda posicion
        rdo = {'La segunda pelicula es': [str(final)]}
        return rdo


    elif nombre_plataforma == 'disney':## si es disney
        movies=data[data['type']=='movie'] #Aca veo las peliculas
        plat=movies[movies['id'].str.startswith('d')] #aAca veo la plataforma indicada
        orden=plat.sort_values(by=['score', 'title'],ascending=[False, True])# Aca Ordeno segun lo solicitado    
        final =  orden.title.iloc[1]## aca me quedo con la segunda posicion
        rdo = {'La segunda pelicula es': [str(final)]}
        return rdo


    elif nombre_plataforma== 'hulu':## si es hulu
        movies=data[data['type']=='movie'] #Aca veo las peliculas
        plat=movies[movies['id'].str.startswith('h')] #aAca veo la plataforma indicada
        orden=plat.sort_values(by=['score', 'title'],ascending=[False, True])# Aca Ordeno segun lo solicitado    
        final =  orden.title.iloc[1]## aca me quedo con la segunda posicion
        rdo = {'La segunda pelicula es': [str(final)]}
        return rdo

    else:
        return('Verifique el valor ingresado')

## Película que más duró según año, plataforma y tipo de duración
## Prueba: get_longest('netflix','min',2016);

@app.get('/get_longest/( {plataforma}, {duracion_type}, {anio})')
async def get_longest( anio: int,duracion:str,nombre_plataforma: str):## los parametros son las plataforma, duration_type y anio

    if nombre_plataforma == 'netflix':## si es netfliz
        nombrep=data[data['id'].str.startswith('n')] #Aca tengo la plataforma ingresada
        if duracion == 'min':## aca filtro si es min, es pelicula
            movies=nombrep[nombrep['type']=='movie'] ## Aca veo solo peliculas, que es la consulta
            year=movies[movies['release_year'] == int(anio)] #Aca tengo el Año ingresado
            tiempo= year.sort_values(by=['duration_int'], ascending= False)## Aca ordeno por tiempo de duracion
            duracionenmin= tiempo.duration_int.values[0] ## respuesta a la consulta de los min de duracion-- el mayor
    
            ## el return indica la posicion, esta ordenado en forma descendente
            return { 'Titulo': tiempo.iloc[0,2], 'duration_int': [int(duracionenmin)] ,'duration_type': [str(duracion)]}
    
        elif duracion == 'season': ## si es season son series y dara las temporadas
       
        
            series= nombrep[nombrep['type']== 'tv show']## aca filtro las series
       
            year=series[series['release_year'] == int(anio)] #Aca tengo el Año ingresado
            tiempo= year.sort_values(by=['duration_int'], ascending= False)## Aca ordeno por tiempo de duracion
            titulo= tiempo.title.values[0] ## respuesta a la consulta del titulo-- el mayor
            duracionenmin= tiempo.duration_int.values[0] ## respuesta a la consulta de los min de duracion-- el mayor
            ## el return indica la posicion, esta ordenado en forma descendente
            rdo = {'Titulo': tiempo.iloc[0,2],'cantidad de min':[int(duracionenmin)],'duration_type':[str(duracion)]}
            return rdo

    elif nombre_plataforma == 'amazon':## si es amazon, repito el proceso
        nombrep=data[data['id'].str.startswith('a')] #Aca tengo la plataforma ingresada
        if duracion == 'min':## aca filtro si es min, es pelicula
            movies=nombrep[nombrep['type']=='movie'] ## Aca veo solo peliculas, que es la consulta
            year=movies[movies['release_year'] == int(anio)] #Aca tengo el Año ingresado
            tiempo= year.sort_values(by=['duration_int'], ascending= False)## Aca ordeno por tiempo de duracion
            duracionenmin= tiempo.duration_int.values[0] ## respuesta a la consulta de los min de duracion-- el mayor
            ## el return indica la posicion, esta ordenado en forma descendente
            rdo = {'Titulo': tiempo.iloc[0,2],'cantidad de min':[int(duracionenmin)],'duration_type':[str(duracion)]}
            return rdo
    
        elif duracion == 'season':## si son series      
            series= nombrep[nombrep['type']== 'tv show']## aca las filtro
            year=series[series['release_year'] == int(anio)] #Aca tengo el Año ingresado
            tiempo= year.sort_values(by=['duration_int'], ascending= False)## Aca ordeno por tiempo de duracion
            duracionenmin= tiempo.duration_int.values[0] ## respuesta a la consulta de los min de duracion-- el mayor
            ## el return indica la posicion, esta ordenado en forma descendente
            rdo = {'Titulo': tiempo.iloc[0,2],'cantidad de min':[int(duracionenmin)],'duration_type':[str(duracion)]}
            return rdo

    elif nombre_plataforma == 'hulu':## si es hulu
        nombrep=data[data['id'].str.startswith('h')] #Aca tengo la plataforma ingresada
        if duracion == 'min':## aca filtro si es min, es pelicula
            movies=nombrep[nombrep['type']=='movie'] ## Aca veo solo peliculas, que es la consulta
            year=movies[movies['release_year'] == int(anio)] #Aca tengo el Año ingresado
            tiempo= year.sort_values(by=['duration_int'], ascending= False)## Aca ordeno por tiempo de duracion
            duracionenmin= tiempo.duration_int.values[0] ## respuesta a la consulta de los min de duracion-- el mayor
            ## el return indica la posicion, esta ordenado en forma descendente
            rdo = {'Titulo': tiempo.iloc[0,2],'cantidad de min':[int(duracionenmin)],'duration_type':[str(duracion)]}
            return rdo
    
        elif duracion == 'season':## si son series              
            series= nombrep[nombrep['type']== 'tv show']## aca las tengo filtradas       
            year=series[series['release_year'] == int(anio)] #Aca tengo el Año ingresado
            tiempo= year.sort_values(by=['duration_int'], ascending= False)## Aca ordeno por tiempo de duracion
            duracionenmin= tiempo.duration_int.values[0] ## respuesta a la consulta de los min de duracion-- el mayor
            ## el return indica la posicion, esta ordenado en forma descendente
            rdo = {'Titulo': tiempo.iloc[0,2],'cantidad de min':[int(duracionenmin)],'duration_type':[str(duracion)]}
            return rdo

    elif nombre_plataforma == 'disney':## si es disney
        nombrep=data[data['id'].str.startswith('d')] #Aca tengo la plataforma ingresada
        if duracion == 'min':## aca filtro si es min, es pelicula
            movies=nombrep[nombrep['type']=='movie'] ## Aca veo solo peliculas, que es la consulta
            year=movies[movies['release_year'] == int(anio)] #Aca tengo el Año ingresado
            tiempo= year.sort_values(by=['duration_int'], ascending= False)## Aca ordeno por tiempo de duracion            
            duracionenmin= tiempo.duration_int.values[0] ## respuesta a la consulta de los min de duracion-- el mayor
            ## el return indica la posicion, esta ordenado en forma descendente
            rdo = {'Titulo': tiempo.iloc[0,2],'cantidad de min':[int(duracionenmin)],'duration_type':[str(duracion)]}
            return rdo
        
        elif duracion == 'season':## si son series      
            series= nombrep[nombrep['type']== 'tv show']## aca las filtro        
            year=series[series['release_year'] == int(anio)] #Aca tengo el Año ingresado
            tiempo= year.sort_values(by=['duration_int'], ascending= False)## Aca ordeno por tiempo de duracion            
            duracionenmin= tiempo.duration_int.values[0] ## respuesta a la consulta de los min de duracion-- el mayor
            ## el return indica la posicion, esta ordenado en forma descendente 
            rdo = {'Titulo': tiempo.iloc[0,2],'cantidad de min':[int(duracionenmin)],'duration_type':[str(duracion)]}
            return rdo
        
        

    else:
        return('Verfique los parametros ingresados')




## Cantidad de Series y Peliculas por rating
#Prueba : get_rating_count('18+')

@app.get('/get_rating_count/({rating})')
async def get_rating_count(rating:str):## el parametro es el rating
    df5= data[data['rating']== rating]## aca filtro x el concepto rating
    res= df5['id'].count()## aca cuentos los id para saber el total
    final= {'rating': [str(rating)], 'Cantidad': [str(res)]}## obtengo mi rdo
    return final



