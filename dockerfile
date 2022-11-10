FROM python:3.9.6

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/keeper
COPY requirements.txt /usr/src/keeper/
RUN pip install -r requirements.txt /usr/src/keeper/
COPY . /usr/src/keeper/

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]