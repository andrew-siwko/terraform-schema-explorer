# terraform-schema-explorer
The goal of this experiment is to explore the provider schema of several cloud providers and my own provider ([text](https://github.com/andrew-siwko/terraform-provider-test)).
The terraform code in this repo requires a number of providers.  `terraform init` will download each provider's executable.
Each provider executable contains its own schema which may be extracted with `terraform providers schema -json`.  
With this information I learn about the cloud providers while building my own provider in go.  The exercise has a nice feedback loop in this regard.
