# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code
COPY . .

# Expose the port for the Flask application
EXPOSE 8080

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]