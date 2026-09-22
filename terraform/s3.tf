resource "aws_s3_bucket" "alert_logs" {
  bucket = "taskflow-alert-logs-${random_id.bucket_suffix.hex}"
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}
