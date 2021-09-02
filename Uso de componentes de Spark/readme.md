<p align="center">
  <img src="fondo.png" />
</p>

### 19 de Agosto del 2021
Como pudimos ver en la clase pasada, Spark es una buena solución cuando se quiere obtener algunas ventajas sobre Hadoop, para poder utilizar esta tecnología, además de configurar el ambiente de trabajo, se deben entender algunos conceptos principales, como la definición de un RDD:

Cada aplicación Spark consta de un programa controlador que ejecuta la función principal del usuario y ejecuta varias operaciones paralelas en un clúster. La principal abstracción que proporciona Spark es un “conjunto de datos distribuido resistente” o mejor dicho, Resilient Distributed Dataset (RDD), lo cual es una colección de elementos particionados en los nodos del clúster que se pueden operar en paralelo. Los RDD se crean comenzando con un archivo en el sistema de archivos Hadoop (o cualquier otro sistema de archivos compatible), o incluso una colección Scala existente en el programa del controlador, y transformándola. Los usuarios también pueden pedirle a Spark que conserve un RDD en la memoria, lo que le permitirá reutilizarlo de manera eficiente en operaciones paralelas. Por último, los RDD se recuperan automáticamente de las fallas de los nodos.

Una segunda abstracción en Spark son las variables compartidas que se pueden usar en operaciones paralelas. De forma predeterminada, cuando Spark ejecuta una función en paralelo como un conjunto de tareas en diferentes nodos, envía una copia de cada variable utilizada en la función a cada tarea. A veces, es necesario compartir una variable entre las tareas o entre las tareas y el programa del controlador. Spark admite dos tipos de variables compartidas: variables de transmisión, que se pueden usar para almacenar en caché un valor en la memoria en todos los nodos, y acumuladores, que son variables a las que solo se "agregan", como contadores y sumas.

En el caso de Python, tenemos a PySpark, la cual es una interfaz para Apache Spark en Python. No solo le permite escribir aplicaciones Spark utilizando las API de Python, sino que también proporciona el shell de PySpark para analizar interactivamente sus datos en un entorno distribuido. PySpark es compatible con la mayoría de las funciones de Spark, como Spark SQL, DataFrame, Streaming, MLlib (aprendizaje automático) y Spark Core.

Los comandos utilizados en clase fueron:
 ```
export SPARK_HOME = ~/spark-3.1.2-bin-hadoop3.2
export PATH = $PATH:$SPARK_HOME/sbin
export PATH = $PATH:$SPARK_HOME/bin


sudo apt install unzip

from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

lines = sc.textFile("file:///home/ubuntu/ml-100k/u.data")
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))

spark-submit  ratings-counter.py
  ```