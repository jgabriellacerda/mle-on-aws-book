FROM 763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:2.5.1-cpu-py311-ubuntu22.04-sagemaker

LABEL maintainer="Kenza AI <support@kenza.ai>"

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         make \
         nginx \
         ca-certificates \
         g++ \
         git \
    && rm -rf /var/lib/apt/lists/*

# PYTHONUNBUFFERED keeps Python from buffering the standard
# output stream, which means that logs can be delivered to the user quickly. 
# PYTHONDONTWRITEBYTECODE keeps Python from writing the .pyc files which are unnecessary in this case. 

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"


WORKDIR /opt/program/
COPY pyproject.toml poetry.lock ./

# Here we get all python packages.
RUN pip install --upgrade pip
RUN pip install flask gevent gunicorn future poetry==2.0.0
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-cache --no-root --without dev && rm -rf /root/.cache
RUN apt-get -y purge --auto-remove git

COPY . /opt/program/

ENTRYPOINT ["executor.sh"]
