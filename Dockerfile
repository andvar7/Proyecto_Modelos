nano Dockerfile

# Indica la imagen base que quieres usar
FROM ubuntu:latest

# Actualiza los paquetes del sistema
RUN apt-get update && apt-get install -y \
    software-properties-common \
    python3 \
    python3-pip

# Copia los archivos de tu aplicación al contenedor
WORKDIR /app
COPY . /app

# Instala las dependencias de tu aplicación
RUN pip3 install -r requirements.txt

# Define el comando por defecto para ejecutar tu aplicación
CMD ["python3", "app.py"]

docker build -t nombre_de_la_imagen .
