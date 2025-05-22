FROM hyperskill.azurecr.io/debian:bullseye

ENV GCC_VERSION 10.2.1-1
ARG PYTHON_VERSION=3.10.13

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libffi-dev \
    liblzma-dev \
    bash \
    cmake \
    curl \
    git \
    gcc=4:${GCC_VERSION} \
    gcc-multilib=4:${GCC_VERSION} \
    g++=4:${GCC_VERSION} \
    make \
    openjdk-17-jdk \
    unzip \
  && rm -rf /var/lib/apt/lists/*

RUN curl https://pyenv.run | bash && \
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && \
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
    . ~/.bashrc && \
    pyenv install $PYTHON_VERSION && \
    pyenv global $PYTHON_VERSION && \
    ln -sf $(pyenv which python) /usr/bin/python3

RUN python3 -m pip install --no-cache \
    https://github.com/hyperskill/hs-test-python/archive/v11.0.28.tar.gz  \
    aiosmtpd  \
    beautifulsoup4  \
    pyyaml

RUN mkdir /checker \
  && curl -L -o /checker/kotlin.zip \
    https://github.com/JetBrains/kotlin/releases/download/v2.0.0/kotlin-compiler-2.0.0.zip \
  && unzip /checker/kotlin.zip -d /checker \
  && apt-get remove -y unzip \
  && rm /checker/kotlin.zip \
  && curl -L -o /checker/hs-test.jar \
    https://github.com/hyperskill/hs-test/releases/download/v12.0.3/hs-test-12.0.3.jar

ENV PATH="/checker/kotlinc/bin:$PATH"

COPY checker /checker/

RUN chmod +x /checker/check.sh
