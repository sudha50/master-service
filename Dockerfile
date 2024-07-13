FROM python:3.8

# Install Unix packages
RUN apt-get update && \
    apt-get -qq -y install curl && \
    apt-get -y install libglib2.0-0 libsm6 libxext6 libxrender-dev

WORKDIR /app
# Copy code
ADD . .
RUN pip install -r requirements.txt


RUN chmod -R 0644 /app
ENV PYTHONPATH=${PYTHONPATH}:.

EXPOSE 8000

ENTRYPOINT ["python", "app.py"]