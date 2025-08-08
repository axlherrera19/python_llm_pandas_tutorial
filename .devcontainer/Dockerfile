# Usar una imagen base de Python
FROM mcr.microsoft.com/devcontainers/python:3.12

# Instalar dependencias adicionales si es necesario
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /workspace

# Copiar requirements.txt si existe
COPY requirements.txt /workspace/requirements.txt

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r /workspace/requirements.txt || true
