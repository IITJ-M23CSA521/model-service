# Dockerfile
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the app code
COPY model_service.py .

# Install dependencies
RUN pip install flask

# Command to run the app
CMD ["python", "model_service.py"]
