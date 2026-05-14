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
    virtualbox_terra_farm = {
      source = 'terra-farm/virtualbox'
    }
    virtualbox_eran_132 = {
      source = 'eran132/vbox
    }
  }
  backend "local" {
    path = "/container_shared/tfstate/schema-explorer.tfstate"
  }
}

provider "linode" {
  token = var.LINODE_API_KEY
}



