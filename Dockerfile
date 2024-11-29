# Use an official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port your application runs on
EXPOSE 8000

# Define the default command to run the application
CMD ["uvicorn", "main:proxy.get_app", "--host", "0.0.0.0", "--port", "8000"]
