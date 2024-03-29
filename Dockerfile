# Utiliza una imagen base de Python
FROM python:3.9.17-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt
COPY dash.py
COPY modelo.pkl

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install pandas==1.5.3
RUN pip install seaborn==0.12.2
RUN pip install matplotlib==3.7.1
RUN pip cache purge
RUN pip install git+https://github.com/andvar7/Proyecto_Modelos.git

# Expone el puerto que utilizará tu aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "dash.py"]
