<p align="center">
  <img src="fondo.png" />
</p>

### 24 de Agosto del 2021
La mayoría de personas que estamos tomando el curso de Big Data es por que recientemente terminamos el curso de Data Analytics, o por otro lado, desde la introducción de este repositorio nos dimos cuenta de que la necesidad de almacenar grandes volúmenes de datos surge como conciencia del análisis de datos que las grandes empresas realizaban para incrementar sus ganancias, entonces, es natural que se busque realizar análisis de datos en volúmenes enormes utilizando las herramientas con las que hemos trabajado anteriormente como Spark o Hadoop, debido a que en la última sesión trabajamos con los componentes de Spark, utilizaremos algunos métodos para el análisis, los métodos los definiremos de la siguiente manera:
#### Reduce()
Realiza una agregación del conjunto de datos de entrada, lo que suele ser un resultado de una función Map
#### Collect()
Devuelve el contenido del RDD sobre el que lo llamamos de vuelta al programa conductor (driver). Habitualmente es un subconjunto de los datos de entrada que hemos transformado y filtrado aplicando alguna de las transformaciones disponibles.
#### Count()
Como se puede suponer devolverá el número total de elementos que hay en un RDD
#### Take(n)
Se trata de una función muy util que permite echar una ojeada a los datos resultantes del proceso al permitir obtener los primeros n elementos del RDD.
#### Transformaciones
Como sugiere el nombre, las transformaciones nos ayudan a transformar los RDD existentes. Como resultado, siempre crean un nuevo RDD que se calcula de forma perezosa. En los ejemplos anteriores, hemos discutido muchas transformaciones, como map(), filter() y reduceByKey().
Las transformaciones son de dos tipos:
Transformaciones estrechas (Narrow transformations)
Transformaciones amplias (Wide transformations)
El código desarrollado en clase fue el siguiente:
```
result = rdd.groupBy(lambda x: x % 2).collect()# [(0, SparkIterable(2,8) )]
print(result)
print([(x, y) for (x, y) in result])
print([(x, list(y)) for (x, y) in result])
print([(x, sorted(y)) for (x, y) in result])
print(sorted([(x, sorted(y)) for (x, y) in result]))



result2 = rdd.groupBy(lambda x: x % 2).mapValues(list).collect()

print(result2)
```