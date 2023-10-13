# Start your image with a node base image
FROM python:3.9-slim

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run hello.py when the container launches
CMD ["python", "matriceMultiplication.py"]