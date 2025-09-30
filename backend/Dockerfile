# Use the official Python 3.8 slim image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 to allow communication
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]