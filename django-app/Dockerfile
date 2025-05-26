FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and app code
COPY requirements.txt ./
COPY Devops/ ./Devops/

# Install dependencies globally (no virtualenv needed inside containers)
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Default command
CMD ["python", "Devops/manage.py", "runserver", "0.0.0.0:8000"]
