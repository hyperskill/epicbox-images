FROM hyperskill.azurecr.io/python:3.10-slim

ARG PYTHON_VERSION=3.10.13

RUN apt-get update && \
    apt-get install -y curl unzip git openjdk-17-jdk && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir /checker && \
    curl -L -o /checker/kotlin.zip \
    https://github.com/JetBrains/kotlin/releases/download/v2.0.0/kotlin-compiler-2.0.0.zip && \
    unzip /checker/kotlin.zip -d /checker && \
    rm /checker/kotlin.zip

RUN curl -L -o /checker/hs-test.jar \
    https://github.com/hyperskill/hs-test/releases/download/v12.0.3/hs-test-12.0.3.jar

RUN python3 -m pip install --no-cache \
    https://github.com/hyperskill/hs-test-python/archive/v11.0.28.tar.gz  \
    aiosmtpd \
    beautifulsoup4 \
    pyyaml

RUN npm install -g https://github.com/hyperskill/sync-input/archive/v1.tar.gz

ENV NODE_PATH=/usr/local/lib/node_modules
ENV PATH="/checker/kotlinc/bin:$PATH"

COPY checker/ /checker/
