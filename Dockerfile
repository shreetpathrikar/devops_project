# Use a Python base image with the desired version
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt
# RUN pip install requests six

# Copy the project files to the working directory
COPY . .

# EXPOSE 3000

# Define the entrypoint for the container
ENTRYPOINT ["python", "app.py"]