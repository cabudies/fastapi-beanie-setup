# Use bitnami/suitecrm as the base image
FROM bitnami/suitecrm

# Set working directory
WORKDIR /app

# Install required packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . /src

# Expose the FastAPI port
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]


