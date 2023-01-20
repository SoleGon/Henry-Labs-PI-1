# Henry-Labs-PI-1
 

## DATA INGINEER
¡Bienvenidos a mi primer proyecto personal de Henry-Data06! 😊

Mi nombre es Mariana Soledad Gonzalez y soy estudiante de Henry Cohorte 06 y les voy a presentar mi primer PI

## RESUMEN

Se nos solicitó como miembros del grupo de datos de una empresa, realizar las transformaciones necesarias sobre un conjunto de datasets y disponibilizar la informacion a traves de la elaboración y ejecución de una Api

# TAREAS

-Realizar una serie de transformaciones sobre los datasets provistos

-Confeccionar 5 consultas solicitadas por el  equipo de datos de la empresa

-Disponibilizar esa información a través de FastApi

-Ejecutar el diploy de la Api

# DESARROLLO

## Transformaciones

Para realizar las transformaciones solicitadas, utilicé las siguientes librerias:

-Pandas

-Numpy

Trabajé sobre los 4 datasets provistos, luego se analizar y realizar las normalizaciones solicitadas en cada uno de ellos, compile toda la informacion en un único dataframe que luego exporte a csv para poder trabajar con todo el set de datos completo. El detalle de éstas operaciones se encuentra en la carpeta "transformaciones".

## Querys

Sobre el csv normalizado mencionado anteriormente, elabore las consultas solicitadas utilizando también las librerias pandas y numpy: las mismas servirán de base para  los pasos siguientes. El detalle del código desarrollado se encuentra en la carpeta "querys"

## FastApi

Para cumplir con disponibilizar las consultas requeridas, utilicé FastApi, ya que es un framework rápido para construir Apis. Trabajé sobre las querys realizadas anteriormente para construir las funciones y luego de instalar FastApi, mediante uvicorn (servidor de alto rendimiento) probé las funciones de manera local, obteniendo un resultado exitoso. El la carpeta "FastApi" se encuentra el archivo main con las funciones y los requirements, junto con el detalle de ésta etapa del proceso

## FastApiDeta

Finalmente para realizar el deploy de la aplicación FastApi, utilicé Deta. Los comandos que fueron ejecutados a traves de la consola power shell de windows son:

- iwr https://get.deta.dev/cli.ps1 -useb | iex
- deta login
- deta new -- fastapideta
- deta deploy
- deta auth disable

En el archivo "fastapideta" se encuentra el archivo main y requirements con el detalle. El resultado del deploy fue exitoso, respondiendo todas las consultas solicitadas correctamente

# LINK DE ACCESO PARA CONSULTAS

Se disponibiliza el link de acceso de Deta para consultas👇


https://vqqswg.deta.dev/


## Video Explicativo



link ☝






# Nos vemos en el proximo proyecto!







![imagen](https://user-images.githubusercontent.com/108495374/213606874-7a466dba-4d4a-45fa-b6a8-d0ae38adda42.jpg)



