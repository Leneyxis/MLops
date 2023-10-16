# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /Mlops

# Copy the current directory contents into the container at /app
COPY . /Mlops

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose the port on which your Flask app will run
EXPOSE 5000

# Define the command to run your application
CMD ["python", "main.py", "--host", "0.0.0.0"]
