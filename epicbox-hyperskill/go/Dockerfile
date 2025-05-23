FROM hyperskill.azurecr.io/python:3.10-slim

ENV GO_VERSION=1.21.0
ENV GO111MODULE=on

RUN apt-get update && \
    apt-get install -y curl bash build-essential unzip openjdk-17-jdk git ca-certificates && \
    curl -L https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz | tar -C /usr/local -xz && \
    ln -s /usr/local/go/bin/go /usr/bin/go && \
    ln -s /usr/local/go/bin/gofmt /usr/bin/gofmt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/local/go/bin:$PATH"

RUN python3 -m pip install --no-cache \
    https://github.com/hyperskill/hs-test-python/archive/v11.0.28.tar.gz  \
    aiosmtpd \
    beautifulsoup4 \
    pyyaml

RUN mkdir /checker  \
    && curl -L -o /checker/kotlin.zip https://github.com/JetBrains/kotlin/releases/download/v2.0.0/kotlin-compiler-2.0.0.zip  \
    && unzip /checker/kotlin.zip -d /checker  \
    && rm /checker/kotlin.zip  \
    && curl -L -o /checker/hs-test.jar https://github.com/hyperskill/hs-test/releases/download/v12.0.3/hs-test-12.0.3.jar

ENV PATH="/checker/kotlinc/bin:$PATH"

COPY checker /checker/

WORKDIR /sandbox

RUN go mod init sandbox && \
    go get github.com/PuerkitoBio/goquery@v1.8.1 \
    github.com/gin-gonic/gin@v1.9.1 \
    github.com/jmoiron/sqlx@v1.3.5 \
    github.com/mattn/go-sqlite3@v1.14.20 \
    go.uber.org/zap@v1.26.0 \
    gopkg.in/yaml.v3@v3.0.1 \
    gorm.io/driver/sqlite@v1.5.4 \
    gorm.io/gorm@v1.25.6

WORKDIR /go

RUN mv /sandbox /sandbox_tmp