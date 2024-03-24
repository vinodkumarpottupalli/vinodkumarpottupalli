FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "dockerdjangoapp/manage.py"]
CMD ["runserver", "127.0.0.1:8000"]