# Como modificaria mi diseño para comunicarme con otro servicio.
## Separación de responsabilidades:
El microservicio actual seguiría manejando la lógica principal (recibir el número y determinar si es par o impar), mientras que un segundo microservicio se encargaría exclusivamente de guardar los resultados en la base de datos. Esto mantiene el principio de bajo acoplamiento, característico de las arquitecturas orientadas a servicios.
## Comunicación entre servicios
Después de generar la respuesta JSON, el servicio principal podría realizar una petición HTTP POST al microservicio de historial, enviando los datos como un objeto JSON.
Por ejemplo, usando una librería como requests para comunicarse con la URL del segundo servicio
## Persistencia y escalabilidad:
El servicio de historial tendría su propia conexión a una base de datos (por ejemplo, PostgreSQL o MongoDB), garantizando la persistencia de datos incluso si el microservicio principal se reinicia o escala en contenedores diferentes.
## Ventajas del diseño:
* Cada microservicio puede evolucionar de forma independiente.
* Facilita el despliegue distribuido (por ejemplo, en Docker o Kubernetes).
* Permite escalar el servicio de historial sin afectar el rendimiento del servicio principal.
