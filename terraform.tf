provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example_instance" {
  instance_type = var.ec2_instance_type
  ami           = var.ec2_image
}

variable "ec2_instance_type" {
  type = string
  description = "Instance type for the server"
  default     = "t2.micro"
}

variable "ec2_image" {
  type = string
  description = "AMI for the server"
  default     = "ami-007855ac798b5175e"
}
