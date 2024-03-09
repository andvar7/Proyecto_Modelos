# Utiliza una imagen base de Python
FROM python:3.9.17-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .
COPY app.py .
COPY modelo.pkl .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que utilizará tu aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
