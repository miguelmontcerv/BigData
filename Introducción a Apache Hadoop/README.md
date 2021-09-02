<p align="center">
  <img src="fondo.png" />
</p>

### 22 de Julio del 2021
Hace algunos meses entré a una conferencia impartida por el ingeniero de big data de la empresa de datos más grande del mundo, Oracle, particularmente el jefe del área de México, y una de las frases que dijo que me llamó más la atención fue: “Saber Hadoop no te convierte en un experto en Big Data, pero si es una de las herramientas más importantes que debes de conocer en este mundo de la tecnología”, fue algo que me pareció interesante porque antes de adentrarme un poco a esta área, había buscado videos en You Tube, de diez videos que me aparecían, 9 eran relacionados a Hadoop, y así como lo dijo ese experto y lo confirmaron aquí en Bedu, Hadoop es solo una herramienta de muchas que existen, en algunas empresas suele ser la principal, entonces, **¿Qué es Hadoop?**
### Hadoop
Hadoop es una estructura de software de código abierto para almacenar datos y ejecutar aplicaciones en clústeres de hardware comercial. Proporciona almacenamiento masivo para cualquier tipo de datos, enorme poder de procesamiento y la capacidad de procesar tareas o trabajos concurrentes virtualmente ilimitados.
### ¿Por qué es importante Hadoop?
* Capacidad de almacenar y procesar enormes cantidades de cualquier tipo de datos, al instante. Con el incremento constante de los volúmenes y variedades de datos, en especial provenientes de medios sociales y la Internet de las Cosas (IoT), ésa es una consideración importante.
* Poder de cómputo. El modelo de cómputo distribuido de Hadoop procesa big data a gran velocidad. Cuantos más nodos de cómputo utiliza usted, mayor poder de procesamiento tiene.
* Tolerancia a fallos. El procesamiento de datos y aplicaciones está protegido contra fallos del hardware. Si falla un nodo, los trabajos son redirigidos automáticamente a otros modos para asegurarse de que no falle el procesamiento distribuido. Se almacenan múltiples copias de todos los datos de manera automática.
* Flexibilidad. A diferencia de las bases de datos relacionales, no tiene que procesar previamente los datos antes de almacenarlos. Puede almacenar tantos datos como desee y decidir cómo utilizarlos más tarde. Eso incluye datos no estructurados como texto, imágenes y videos.
* Bajo costo. La estructura de código abierto es gratuita y emplea hardware comercial para almacenar grandes cantidades de datos.
* Escalabilidad. Puede hacer crecer fácilmente su sistema para que procese más datos son sólo agregar nodos. Se requiere poca administración.

Ahora que logramos entender que es Hadopp y sus ventajas, vamos a ver una parte muy importante de esta herramienta, **¿Qué es el YARN?** 
Apache Hadoop YARN es la tecnología de gestión de recursos y programación de trabajos en el marco de procesamiento distribuido de código abierto Hadoop. YARN, uno de los componentes centrales de Apache Hadoop, es responsable de asignar recursos del sistema a las diversas aplicaciones que se ejecutan en un clúster de Hadoop y programar tareas para que se ejecuten en diferentes nodos del clúster.

El término YARN proviene de las siglas de Yet Another Resource Negotiator, pero comúnmente se lo denomina solo por el acrónimo; el nombre completo era humor autocrítico por parte de sus desarrolladores. La tecnología se convirtió en un subproyecto de Apache Hadoop dentro de Apache Software Foundation (ASF) en 2012 y fue una de las características clave agregadas en Hadoop 2.0, que se lanzó para pruebas ese año y estuvo disponible de forma generalizada en octubre de 2013.

La adición de YARN expandió significativamente los usos potenciales de Hadoop. La encarnación original de Hadoop emparejó estrechamente el Sistema de archivos distribuido de Hadoop (HDFS) con el marco de programación y el motor de procesamiento MapReduce orientado por lotes, que también funcionó como administrador de recursos y programador de trabajos de la plataforma de big data. Como resultado, los sistemas Hadoop 1.0 solo podían ejecutar aplicaciones MapReduce —una limitación que Hadoop YARN eliminó.

*Algunos comandos que se utilizaron en clase fueron:*

```
$ hadoop fs -mkdir /user/USERNAME/wordcount
$ hadoop fs -mkdir /user/USERNAME/wordcount/input
$ hadoop fs -put /bluearc/data/schatz/data/textmining/bible+shakes.nopunc/user/mschatz/wordcount/input

```

## Ahora vamos a contar las palabras:
```
$ hadoop jar /usr/lib/hadoop/hadoop-examples.jar wordcount \
             /user/USERNAME/wordcount/input \
             /user/USERNAME/wordcount/output
```             
             
Ahora decarga los resultados a tu repo principal

```
$ hadoop fs -get /user/USERNAME/wordcount/output output
```