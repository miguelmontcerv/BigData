<p align="center">
  <img src="fondo.png" />
</p>

### 29 de Julio del 2021
**HDFS (Hadoop Distributed File System)** es el componente principal del ecosistema Hadoop. Esta pieza hace posible almacenar data sets masivos con tipos de datos estructurados, semi-estructurados y no estructurados como imágenes, vídeo, datos de sensores, etc. Está optimizado para almacenar grandes cantidades de datos y mantener varias copias para garantizar una alta disponibilidad y la tolerancia a fallos. Con todo esto, HDFS es una tecnología fundamental para Big Data, o dicho de otra forma, es el Big Data File System o almacenamiento Big Data por excelencia.

Es un sistema distribuido basado en Java que permite obtener una visión de los recursos como una sola unidad. Para ello crea una capa de abstracción como un sistema de ficheros único. HDFS se encarga de almacenar los datos en varios nodos manteniendo sus metadatos. Distribuir los datos en varios nodos de almacenamiento aumenta la velocidad de procesamiento, el paralelismo en las operaciones y permite la replicación de los datos.

Está basado en la idea de que mover el procesamiento es mucho más rápido, fácil y eficiente que mover grandes cantidades de datos, que pueden producir altas latencias y congestión en la red. HDFS proporciona a las aplicaciones la capacidad de acceder a los datos en el lugar en el que se encuentren almacenados.
##### Caracteristicas
En HDFS, los ficheros que se almacenan son divididos en bloques de un mismo tamaño (128 MB) y estos se distribuyen en los nodos que forman el clúster. Esta característica hace que el sistema de ficheros no funcione de forma óptima con ficheros pequeños, por lo que deben evitarse. El tamaño de bloque es configurable.
Para conseguir una alta escalabilidad, HDFS usa almacenamiento local que escala horizontalmente. Aumentar el espacio de almacenamiento solamente supone añadir discos duros a nodos existentes o añadir más nodos al sistema. Estos servidores tienen un coste reducido, al tratarse de hardware básico con almacenamiento conectado. HDFS soporta miles de nodos, lo más típico en un cluster es desplegar decenas o cientos de nodos y manejar cientos de terabytes, con la capacidad de escalar a decenas de petabytes

Para mantener la integridad de los datos, HDFS almacena por defecto 3 copias de cada bloque de datos. Esto significa que el espacio necesario en HDFS es el triple, por lo que el coste también aumenta. Aunque la replicación de datos no es necesaria para el funcionamiento de HDFS, almacenar solamente una copia podría suponer pérdida de datos frente a fallos o corrupción de ficheros, eliminando la durabilidad del dato.

Algunos comandos que ejecutamos en clase fueron:
 ```
>bin/hadoop dfs -mkdir /test

>bin/hadoop dfs -ls /

>bin/hadoop dfs -put README.txt /test

>bin/hadoop dfs -ls /test

Found 1 items
-rw-r--r--   1 srinath supergroup       1366 2012-04-10 07:06 /test/README.txt
 ```
