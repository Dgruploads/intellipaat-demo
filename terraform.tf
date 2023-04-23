provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example_instance" {
  instance_type = "t2.micro"
  ami           = "ami-007855ac798b5175e"
}
