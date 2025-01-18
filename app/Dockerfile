# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM docker.io/bitnami/python:3.12-debian-12 AS builder

WORKDIR /src
COPY requirements.txt /src
RUN --mount=type=cache,target=/root/.cache/pip \
pip3 install -r requirements.txt -i https://mirrors.sustech.edu.cn/pypi/web/simple

COPY . .

CMD ["python3", "server.py"]

FROM builder as dev-envs

# 替换为 USTC 的 Debian 镜像源
RUN sed -i 's|deb.debian.org|mirrors.ustc.edu.cn|g' /etc/apt/sources.list && \
sed -i 's|security.debian.org|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list && \
apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN groupadd -r docker && \
    useradd -r -s /bin/bash -g docker vscode

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /

CMD ["python3", "server.py"]