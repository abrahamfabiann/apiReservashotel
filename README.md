# API del Sistema de Reservas de Hotel

Este API fue desarrollado para un Sistema de Reservas de Hotel, utilizando Django y Django REST Framework. La API cuenta con endpoints para gestionar reservas, habitaciones, clientes, tipos de habitación y métodos de pago.

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