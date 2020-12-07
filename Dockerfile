FROM python:3.8

EXPOSE 8000

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt
RUN pip install cryptography

COPY . /app

ENTRYPOINT ["python"]
CMD ["app/main.py"]
