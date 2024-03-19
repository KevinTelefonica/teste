FROM lurivaen/dockercourse:latest

# Definindo o diretório onde a aplicação será armazenada
WORKDIR /app

# Copiar os arquivos da pasta local para dentro do container
COPY . /app
# Garante que será iniciado a aplicação.
CMD ["python", "app.py"]
