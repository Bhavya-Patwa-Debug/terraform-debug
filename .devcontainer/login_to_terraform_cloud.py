"""Script to login to Terraform Cloud from a Codespace."""

import json
import os
from pathlib import Path

from colorama import Fore, Style


def print_green(text: str) -> None:
    """Print text in green."""
    print(Fore.GREEN + text + Style.RESET_ALL)


def print_red(text: str) -> None:
    """Print text in red."""
    print(Fore.RED + text + Style.RESET_ALL)


# Try to get the Terraform Cloud API token from the environment
token = os.environ.get("TERRAFORM_CLOUD_API_TOKEN")
if not token:
    print_red(
        "Can't login to Terraform Cloud: missing TERRAFORM_CLOUD_API_TOKEN environment variable"
    )
    print_red("To generate a token, go to https://app.terraform.io/app/settings/tokens")
    print_red(
        "To set a secret in Codespaces, go to  https://github.com/settings/codespaces/secrets/new"
    )
    exit(0)

credentials = {
    "credentials": {
        "app.terraform.io": {
            "token": token,
        }
    }
}

path = Path("/home/vscode/.terraform.d/credentials.tfrc.json")

# Create the directory if it doesn't exist
path.parent.mkdir(parents=True, exist_ok=True)

with open(path, "w") as f:
    f.write(json.dumps(credentials))

print_green("Successfully created Terraform Cloud credentials file.")
