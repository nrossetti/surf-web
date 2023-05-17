# Use the official Python base image with the desired version
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code to the container
COPY . .

# Expose the port on which your Flask app runs
EXPOSE 5000

# Set the environment variable to run the Flask app
ENV FLASK_APP=app.py

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]