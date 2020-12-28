FROM python:3.6-alpine
COPY . /src
WORKDIR /src
RUN pip install --no-cache-dir -r requirements.txt 
ENTRYPOINT ["python","run.py"]