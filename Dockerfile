# Use Python 3.9 slim version as the base image
FROM python:3.9-slim

# Install necessary packages, including awscli
RUN apt-get update -y && apt-get install -y awscli && apt-get clean

# Set the working directory
WORKDIR /app

# Copy the contents of the current directory to /app inside the container
COPY . /app

# Upgrade pip to the latest version and install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the main application
CMD ["python3", "main.py"]
