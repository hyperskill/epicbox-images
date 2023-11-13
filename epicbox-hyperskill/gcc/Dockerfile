FROM hyperskill.azurecr.io/epicbox/debian:bullseye

ENV GCC_VERSION 10.2.1-1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc=4:${GCC_VERSION} gcc-multilib=4:${GCC_VERSION} g++=4:${GCC_VERSION} \
    make cmake python3 python3-dev python3-pip curl bash \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install https://github.com/hyperskill/hs-test-python/archive/refs/tags/v11.0.0.tar.gz

RUN mkdir /checker && \
    curl -L -o /checker/kotlin.zip \
    https://github.com/JetBrains/kotlin/releases/download/v1.9.10/kotlin-compiler-1.9.10.zip && \
    apt-get update && apt-get install -y unzip && \
    unzip /checker/kotlin.zip -d /checker && \
    rm /checker/kotlin.zip && \
    apt-get remove -y unzip && \
    rm -rf /var/lib/apt/lists/*

RUN curl -L -o /checker/hs-test.jar \
    https://github.com/hyperskill/hs-test/releases/download/v11.0.0/hs-test-v11.0.0.jar

ENV PATH="/checker/kotlinc/bin:$PATH"

COPY checker /checker/
