# Define the AWS account ID
account_id = "123456789012"

# Define the project name
project_name = "cloud_project"

# Concatenate strings to form the S3 bucket name
bucket_name = account_id + '-' + project_name + "-bucket"


# Print the resulting bucket name
print(f"S3 Bucket Name: {bucket_name}")



# EXERCISE EC2 STRING CONCATENATION

# Environment name prod, dev, staging
environment = "production"

# application name
application_name = "web_app"

# instance number
instance_number = "123456789"

# Concatenate strings to form EC2 String Concatenantion Name

EC2_string = environment + "-" + application_name + "-" + instance_number

# Print the resulting EC2 string name

print(f"EC2 String name: {EC2_string}")