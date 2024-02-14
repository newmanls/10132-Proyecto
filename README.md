# Preparación del entorno de desarrollo

## Requisitos

- git
- Python3
- MariaDB

## Descarga el repositorio

```sh
git clone https://[usuario de github]@github.com/newmanls/10132-Proyecto
```

Ejemplo:

```sh
git clone https://newmanls@github.com/newmanls/10132-Proyecto
```

Luego, se puede navegar dentro de la carpeta del repositorio con:

```sh
cd 10132-Proyecto
```

## MariaDB

Al instalar MariaDB, se debe tener en cuenta los siguientes ajustes para que la conexión con Django funcione correctamente.

| Ajuste     | Valor  |
| ---        | ---    |
| Puerto     | 3306   |
| Usuario    | root   |
| Contraseña | 123456 |

Una vez instalado MariaDB, se debe crear la tabla `unexca`.

## Entorno virtual de Python

Los entornos virtuales se pueden describir como directorios de instalación aislados. Este aislamiento te permite localizar la instalación de las dependencias de tu proyecto, sin obligarte a instalarlas en todo el sistema.

### Instalación de virtualenv

Para trabajar con un entorno virtual, se debe instalar el paquete de Python `virtualenv`, una herramienta que se utiliza para crear entornos Python aislados. Crea una carpeta que contiene todos los ejecutables necesarios para usar los paquetes que necesitaría un proyecto de Python.

> Nota: Este paso sólo se debe hacer una vez.

```sh
python -m pip install virtualenv
```

Si se presenta el error `No module named pip`, se ejecuta el siguiente comando:

```sh
python -m ensurepip --upgrade
```

### Creación del entorno

Desde el directorio del proyecto, se accede al directorio `src`. Luego, se ejecuta el siguiente comando para crear el entorno virtual con el que se va a trabajar.

> Nota: Este paso sólo se debe hacer una vez.

```sh
cd src
python -m venv venv
```

### Activación del entorno virtual

Cada vez que se vaya a trabajar en el proyecto, se debe activar el entorno virtual de Python, según el sistema que se esté utilizando.

```sh
venv\Scripts\activate.bat  # En Windows CMD
venv\Scripts\Activate.ps1  # En Windows PowerShell
source venv/Scripts/activate  # En Windows Git Bash
source venv/bin/activate  # En Linux
```

### Instalación de dependencias

El proyecto requiere una serie de paquetes para funcionar. Para instalarlos, se usa el siguiente comando:

```sh
python -m pip install -r requirements.txt
```

### Desactivación del entorno virtual

Una vez se termine de trabajar en el proyecto, el entorno virtual se puede desactivar con el siguiente comando.

```sh
deactivate
```

## Django

### Migraciones

Al descargar el repositorio o al hacer cambios en los modelos se debe hacer las migraciones correspondiente para la actualización de la base de datos:

```sh
python manage.py makemigrations
python manage.py migrate
```

### Creación del superusuario

Django cuenta con un panel administrativo, la cual puede ser usada para crear, consultar, actualizar y borrar registros de los modelos, comunicándose directamente con la base de datos. Para acceder a dicho panel se requiere un superusuario. Para crearlo, se ejecuta el siguiente comando.

```sh
python manage.py createsuperuser
```

Con el servidor ejecutándose, se puede acceder al panel de administración de Django desde: <http://127.0.0.1:8000/admin>.

### Ejecutando el proyecto

En la carpeta `src` y corriendo el entorno virtual ya configurado, se ejecuta:

```sh
python manage.py runserver
```

La ruta predeterminada para acceder al sistema es: <http://127.0.0.1:8000/>.
