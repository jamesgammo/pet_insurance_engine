# Use a minimal Python 3.11 image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Ensure the /code directory exists (not really needed unless used later)
RUN mkdir -p /code 

# Copy and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Copy the application code to /app
COPY ./app .

# Run FastAPI using Uvicorn
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
