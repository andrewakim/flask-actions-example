FROM python:3.7-slim-buster

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PYTHONUNBUFFERED=0 \
    FLASK_APP=app.py \
    FLASK_ENV=development

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
 && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip3 install --no-cache-dir -r requirements.txt \
  && rm -rf /root/.cache/pip/*

COPY . /code

ENTRYPOINT ["/bin/bash", "/code/entrypoint.sh"]
