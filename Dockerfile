FROM python:3.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

EXPOSE 8000

# ENTRYPOINT ["python"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
