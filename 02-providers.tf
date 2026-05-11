terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
    }
    digitalocean = {
      source  = "digitalocean/digitalocean"
    }
    google = {
      source  = "hashicorp/google"
    }
    ibm = {
      source  = "IBM-Cloud/ibm"
    }
    linode = {
      source = "linode/linode"
    }
    oci = {
      source  = "oracle/oci"
    }
    time = {
      source = "hashicorp/time"
    }
  }
  backend "local" {
    path = "/container_shared/tfstate/schema-explorer.tfstate"
  }
}

provider "linode" {
  token = var.LINODE_API_KEY
}

