variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Project name used for resource naming"
  type        = string
  default     = "taskflow"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "db_name" {
  description = "RDS database name"
  type        = string
  default     = "taskflow"
}

variable "db_username" {
  description = "RDS database username"
  type        = string
  default     = "taskflow"
}

variable "db_password" {
  description = "RDS database password"
  type        = string
  sensitive   = true
}
