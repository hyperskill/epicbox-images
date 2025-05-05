FROM hyperskill.azurecr.io/node:18.20.4-bullseye-slim

ARG PYTHON_VERSION=3.10.13

RUN apt-get update && \
    apt-get install -y curl unzip wget git openjdk-17-jdk make build-essential \
    libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
    gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 \
    libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 \
    libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 \
    libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 \
    libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates \
    fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils && \
    apt-get clean && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

RUN curl https://pyenv.run | bash && \
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && \
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
    . ~/.bashrc && \
    pyenv install $PYTHON_VERSION && \
    pyenv global $PYTHON_VERSION && \
    ln -sf $(pyenv which python) /usr/bin/python3

RUN mkdir /checker && \
    curl -L -o /checker/kotlin.zip \
    https://github.com/JetBrains/kotlin/releases/download/v2.0.0/kotlin-compiler-2.0.0.zip && \
    unzip /checker/kotlin.zip -d /checker && \
    rm /checker/kotlin.zip

RUN curl -L -o /checker/hs-test.jar \
    https://github.com/hyperskill/hs-test/releases/download/v12.0.3/hs-test-12.0.3.jar

RUN python3 -m pip install --no-cache \
    https://github.com/hyperskill/hs-test-python/archive/v11.0.26.tar.gz

RUN npm install -g https://github.com/hyperskill/sync-input/archive/v1.tar.gz

ENV NODE_PATH=/usr/local/lib/node_modules
ENV PATH="/checker/kotlinc/bin:$PATH"

COPY checker/ /checker/

COPY sandbox/ /sandbox/