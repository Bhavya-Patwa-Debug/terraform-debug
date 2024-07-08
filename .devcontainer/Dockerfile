# Start from a base image for python. (https://github.com/microsoft/vscode-dev-containers/tree/main/containers/python-3)
# https://mcr.microsoft.com/v2/vscode/devcontainers/python/tags/list
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Install Terraform CLI (as root)
# Ref: https://www.terraform.io/downloads
# Ref: https://www.hashicorp.com/official-packaging-guide
# ? Download the signing key to a new keyring
RUN wget --quiet -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
# ? Add the HashiCorp repo
RUN echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
# ? Install pinned version
# Available versions: https://github.com/hashicorp/terraform/tags
RUN apt-get update \
    && apt-get install -y --no-install-recommends terraform=1.3.9 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Change user (non-root user for Codespace)
USER vscode