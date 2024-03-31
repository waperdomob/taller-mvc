# taller-mvc

# Registro de Clientes API

Este proyecto es una API RESTful desarrollada con Django Rest Framework para gestionar el registro de clientes.

## Funcionamiento

La API permite realizar las siguientes operaciones sobre los datos de clientes:

- Crear un nuevo cliente
- Leer la información de un cliente existente
- Actualizar la información de un cliente
- Eliminar un cliente

Los datos de los clientes incluyen nombre completo, número de documento, correo electrónico, fecha de nacimiento y fechas de registro y actualización.

## Instrucciones de Ejecución

Siga estos pasos para ejecutar el proyecto en su entorno local:

1. Clonar el repositorio:

```bash
git clone https://github.com/waperdomob/taller-mvc

# instalar dependencias
cd tallermvc
pip install -r requirements.txt

# Aplicar las migraciones a la base de datos.
python manage.py migrate

# Ejecutar el servidor del desarrollo.
python manage.py runserver

``` 
La API estará disponible en http://127.0.0.1:8000/.

Una vez que el servidor esté en funcionamiento, puede interactuar con la API utilizando herramientas como cURL, Postman o simplemente un navegador web.

Para obtener una lista de todos los clientes: GET /clients/
Para crear un nuevo cliente: POST /clients/
Para obtener detalles de un cliente específico: GET /clients/{id}/
Para actualizar los detalles de un cliente existente: PUT /clients/{id}/
Para eliminar un cliente: DELETE /clients/{id}/
Reemplace {id} con el ID del cliente correspondiente.

