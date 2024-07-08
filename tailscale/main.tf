terraform {
  required_version = ">= 1.0.0"

  cloud {
    organization = "bhavya-debug"
    workspaces {
      name = "terraform-debug"
    }
  }

  required_providers {
    tailscale = {
      source  = "tailscale/tailscale"
      version = "~> 0.16.1"
    }
  }
}
