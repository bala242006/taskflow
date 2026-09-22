data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "../lambda/index.py"
  output_path = "../lambda/lambda.zip"
}

resource "aws_iam_role" "lambda_role" {
  name = "taskflow-alert-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "lambda_policy" {
  name = "taskflow-alert-lambda-policy"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:PutObject"
        ]
        Resource = "${aws_s3_bucket.alert_logs.arn}/*"
      },
      {
        Effect = "Allow"
        Action = [
          "sns:Publish"
        ]
        Resource = aws_sns_topic.alerts.arn
      },
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "*"
      }
    ]
  })
}

resource "aws_lambda_function" "alert_handler" {
  function_name = "taskflow-alert-handler"
  role          = aws_iam_role.lambda_role.arn
  handler       = "index.lambda_handler"
  runtime       = "python3.12"

  filename         = data.archive_file.lambda_zip.output_path
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
}

resource "aws_lambda_function_url" "alert_handler" {
  function_name      = aws_lambda_function.alert_handler.function_name
  authorization_type = "NONE"
}

resource "aws_lambda_permission" "function_url" {
  statement_id           = "AllowFunctionURLInvoke"
  action                 = "lambda:InvokeFunctionUrl"
  function_name          = aws_lambda_function.alert_handler.function_name
  principal              = "*"
  function_url_auth_type = "NONE"
}

output "lambda_function_url" {
  value = aws_lambda_function_url.alert_handler.function_url
}
