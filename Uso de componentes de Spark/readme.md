<p align="center">
  <img src="fondo.png" />
</p>

En esta que es nuestra última sesión, hablaremos de una de las mejores bases de datos que existen hoy en día, pero para eso primero debemos definir la diferencia entre los tipos de datos, tenemos aquellos que son Relacionales y No relacionales:
### Relacionales

Son una colección de elementos de datos organizados en un conjunto de tablas formalmente descritas, desde donde se puede acceder a los datos o volver a montarlos de muchas maneras diferentes sin tener que reorganizar las tablas de la base. La interfaz estándar de programa de usuario y aplicación a una base de datos relacional, es el Lenguaje de Consultas Estructuradas (SQL). Los comando SQL se utilizan tanto para consultas interactivas como para obtener información de una base de datos relacional y la recopilación de datos para informes.

Las bases de datos relacionales se basan en la organización de la información en partes pequeñas que se integran mediante identificadores; a diferencia de las bases de datos no relacionales que, como su nombre lo indica, no tienen un identificador que sirva para relacionar dos o más conjuntos de datos. Además, son más robustas, es decir, tienen mayor capacidad de almacenamiento, y son menos vulnerables ante fallas, estas son sus principales características.
### No Relacionales
Están diseñadas específicamente para modelos de datos específicos y tienen esquemas flexibles para crear aplicaciones modernas. Son ampliamente reconocidas porque son fáciles de desarrollar, tanto en funcionalidad como en rendimiento a escala. Usan una variedad de modelos de datos, que incluyen documentos, gráficos, clave-valor, en-memoria y búsqueda.

Las bases de datos no relacionales (NoSQL) son las que, a diferencia de las relacionales, no tienen un identificador que sirva de relación entre un conjunto de datos y otros. Como veremos, la información se organiza normalmente mediante documentos y es muy útil cuando no tenemos un esquema exacto de lo que se va a almacenar.

Con relación a formatos, la información de una base de datos puede ser almacenada en tablas o documentos. Cuando los datos son organizados en un archivo de Excel, es en formato tabla, pero cuando simplemente son datos escritos como cartas, fórmulas o recetas, son datos en formato documento. Esto aplica para los dos tipos de bases de datos.

Habitualmente los datos almacenados en tablas son bases de datos relacionales, porque existe la posibilidad de enlazar los datos de una tabla con los de otra y los datos almacenados en documentos son no relacionales, aunque no siempre tiene que ser así. Por ejemplo, los datos de una tabla pueden ser transcritos a un documento, todo depende del punto de vista y la necesidad del problema que se vaya enfrentar.

### NoSQL: Apache Cassandra
Como te podrás haber dado cuenta, al usar una cantidad torrencial de datos, no podemos alojar nuestros datos en un único servidor, y por tanto, el SQL clásico al cual estamos acostumbrados de toda la vida, es insuficiente para cubrir las demandantes tareas que exige el Big Data: NoSQL es el siguiente paso, ya que entre muchos factores, debes recordar que SQL es escalable verticalmente, por lo tanto, resulta mucho más díficil de manejar Big Data; NoSQL es escalable horizontalmente.


Los comandos utilizados en clase fueron:
 ```
CREATE KEYSPACE test_keyspace WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 1};

DESCRIBE keyspaces;

USE test_keyspace;

CREATE TABLE company_employees (
company text,
empoyee_name text,
employee_age int,
job text,
PRIMARY KEY (company, empoyee_name)
);

describe tables;

INSERT INTO company_employees (company, empoyee_name ,employee_age, job ) VALUES ( 'Microsoft', 'Juan', 45, 'Analista de Contenido');
INSERT INTO company_employees (company, empoyee_name ,employee_age, job ) VALUES ( 'Amazon', 'Pablo', 49, 'Contador');
  ```