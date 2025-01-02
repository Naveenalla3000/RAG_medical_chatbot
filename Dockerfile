FROM python:3.12.8
WORKDIR /app
COPY requirements.txt .
COPY . .
RUN pip install -r requirements.txt -q
COPY . .
CMD ["chainlit", "run", "app.py", "--host","0.0.0.0", "--port", "8000"]