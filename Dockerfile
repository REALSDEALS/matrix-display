# Matrix | Dockerfile: | REALSDEALS

# Using Python 3.11 (lightweight):
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Installing Dependencies:
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 5000 (Flask:)
EXPOSE 5000

# Command to run the application when the container starts
CMD ["python", "app.py"]
