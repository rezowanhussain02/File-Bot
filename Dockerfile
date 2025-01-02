# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot code
COPY . .

# Expose the default port (optional, adjust if needed)
EXPOSE 3000

# Command to run the bot
CMD ["python3", "main.py"]
