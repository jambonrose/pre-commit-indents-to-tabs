terraform {

  required_version = ">=1.1"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>2.92"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = var.project
  location = var.resource_group_location
}
