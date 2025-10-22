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


# Instrucciones para ejecutar el microservicio Flask

## 1. Clonar el repositorio
Clona el repositorio en tu máquina local usando:

## 2. Crea un entorno virtual
Crea un entorno virtual de Python (para aislar las dependencias del proyecto):
python -m venv .venv

## 3. Instalar dependencias
Instala Flask y las demás dependencias desde el archivo requirements.txt:
pip install -r requirements.txt

## 4. Ejecutar la aplicación
Ejecuta el microservicio con:
python app.py
Esto iniciará el servidor en la dirección:
http://127.0.0.1:5000

## 5. Probar el microservicio

Abre tu navegador o usa una herramienta como Postman e ingresa la URL:
http://127.0.0.1:5000/numero/<num>
Por ejemplo:
http://127.0.0.1:5000/numero/6
y ahi podras ver como funciona este servicio :)


##
