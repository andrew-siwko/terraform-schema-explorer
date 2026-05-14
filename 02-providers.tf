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
    equinix = {
      source = "equinix/equinix"
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
    mirror = {
      source = "andrew/property-mirror"
    }
    oci = {
      source  = "oracle/oci"
    }
    proxmox = {
      source = "bpg/proxmox"
    }
    time = {
      source = "hashicorp/time"
    }
    virtualbox-terra-farm = {
      source = "terra-farm/virtualbox"
      version = "0.2.2-alpha.1"
    }
    virtualbox-eran-132 = {
      source = "eran132/vbox"
    }
    virtualbox-aslafy-zero = {
      source = "aslafy-z/virtualbox"
    }
  }
  backend "local" {
    path = "/container_shared/tfstate/schema-explorer.tfstate"
  }
}

provider "linode" {
  token = var.LINODE_API_KEY
}



