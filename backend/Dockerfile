FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./req.txt . 

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r req.txt

# Copy the rest of the application code into the container at /app
COPY ./scripts/ .

EXPOSE 5000

# Start the Flask application when the container starts

CMD ["gunicorn", "urls:app", "-b", "0.0.0.0:5000"]

# CMD ["python", "urls.py"]