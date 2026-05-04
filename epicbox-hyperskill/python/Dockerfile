FROM hyperskill.azurecr.io/python:3.14-slim

ENV INSIDE_DOCKER=1

RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
      bc \
      curl \
      git \
      sqlite3 \
      wget \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache \
  https://github.com/hyperskill/hs-test-python/archive/v11.0.32.tar.gz \
  GitPython==3.1.27

COPY checker/ /checker/
