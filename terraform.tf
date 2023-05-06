provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example_instance" {
  instance_type = var.ec2_instance_type
  ami           = "ami-007855ac798b5175e"
  tags          = local.name
}

locals {
  name = "some_name"
  project = "some_project"
}

variable "ec2_instance_type" {
  description = "Instance type for the EC2 instance"
  type        = string
}
