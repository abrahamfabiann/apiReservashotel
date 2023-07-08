# API del Sistema de Reservas de Hotel

Este API fue desarrollado para un Sistema de Reservas de Hotel, utilizando Django y Django REST Framework. La API cuenta con endpoints para gestionar reservas, habitaciones, clientes, tipos de habitación y métodos de pago.

# API del Sistema de Reservas de Hotel
Este API fue desarrollado para un Sistema de Reservas de habitaciones de un hotel, utilizando Django, Django REST Framework y SQLite. La API cuenta con endpoints para gestionar reservas, habitaciones, clientes, tipos de habitación y métodos de pago.

### Ejecucion de proyecto Django Rest Framework

1. Abrir una terminal y clonar el repositorio
```sh
git clone https://github.com/abrahamfabiann/apiReservashotel.git
```

2. Ingresar al directorio
```sh
cd apiReservashotel
```
3. Creamos la imagen
```sh
docker build -t api-reservas-hotel .
```
4. Iniciamos un nuevo contenedor
```sh
docker run -p 8000:8000 api-reservas-hotel
```
5. Ingresamos a la siguiente direccion y ya tenemos corriendo nuestro proyecto

http://localhost:8000/

donde tenemos lo siguiente: 

- admin/		*Sitio de administracion de Django*
- api/		*Contiene los endpoints del proyecto*
- docs/		*Documentacion autogenerado de endpoints*

### Correr Endpoints

Para tener corriendo los endpoints requerimos ejecutar las migraciones dentro del contenedor,
para esto realizamos lo siguiente:
1. Abrir en una segunda terminal y ejecutar el siguiente comando para recuperar el identificador del contenedor
```sh
docker ps
```
2. Copiamos el CONTAINER ID y ejecutamos el comando
para usuarios linux
```sh
docker exec -it xxxxxxxx bash
```
para usuarios windows
```sh
winpty docker exec -it xxxxxxxx bash
```
3. Una vez dentro del contenedor ejecutamos
```sh
python manage.py migrate
```

Ahora nuevamente ingresamos a la direccion:

http://localhost:8000/api


BUEN TRABAJO! ya tenemos corriendo nuestra API

## Endpoints

Los siguientes endpoints están disponibles en la API:

### Endpoints de Tipo de Habitación:
- GET /api/room-types/
- GET /api/room-types/{id}/
- POST /api/room-types/
- PUT /api/room-types/{id}/
- DELETE /api/room-types/{id}/

### Endpoints de Método de Pago:
- GET /api/payment-methods/
- GET /api/payment-methods/{id}/
- POST /api/payment-methods/
- PUT /api/payment-methods/{id}/
- DELETE /api/payment-methods/{id}/

### Endpoints de Habitación:
- GET api/rooms/
- GET /api/rooms/{id}/
- POST /api/rooms/
- PUT /api/rooms/{id}/
- DELETE /api/rooms/{id}/

### Endpoints de Cliente:
- GET /api/customers/
- GET /api/customers/{id}/
- POST /api/customers/
- PUT /api/customers/{id}/
- DELETE /api/customers/{id}/

### Endpoints de Reserva:
- GET /api/reservations/
- GET /api/reservations/{id}/
- POST /api/reservations/
- PUT /api/reservations/{id}/
- DELETE /api/reservations/{id}/

## Justificación

Los endpoints están diseñados para proporcionar funcionalidad completa de CRUD (Crear, Leer, Actualizar, Eliminar) para cada modelo en el Sistema de Reservas de Hotel. La justificación de cada endpoint es la siguiente:

- **Endpoints de Tipo de Habitación:** Estos endpoints manejan los tipos de habitación disponibles en el hotel, proporcionando la capacidad de listar, crear, actualizar y eliminar tipos de habitación.

- **Endpoints de Método de Pago:** Estos endpoints administran los métodos de pago aceptados por el hotel, incluyendo funcionalidades para listar, crear, actualizar y eliminar métodos de pago.

- **Endpoints de Habitación:** Estos endpoints manejan las habitaciones del hotel, permitiendo a los usuarios obtener una lista de todas las habitaciones, crear nuevas habitaciones, actualizar detalles de habitaciones existentes y eliminar habitaciones.

- **Endpoints de Cliente:** Estos endpoints permiten gestionar la información de los clientes. Los usuarios pueden obtener una lista de todos los clientes, crear nuevos registros de clientes, actualizar detalles de clientes y eliminar registros de clientes.

- **Endpoints de Reserva:** Estos endpoints se encargan de gestionar las reservas. Los usuarios pueden ver todas las reservas, crear nuevas reservas, actualizar reservas existentes y eliminar reservas. Ademas que se maneja los diferentes estados de reserva, como "Pendiente", "Pagado" y "Cancelado".

Al proporcionar estos endpoints, la API facilita la integración del Sistema de Reservas de Hotel con aplicaciones cliente(Frontend), permitiéndoles realizar todas las operaciones necesarias relacionadas con las reservas, habitaciones, clientes, tipos de habitación y métodos de pago.

## Documentacion automatica

La documentacion automatica es generada con 'coreapi' el cual se encuentra en el siguiente enlace:

- GET /docs/