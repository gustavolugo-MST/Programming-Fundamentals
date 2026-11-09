# Single quotes
single_quotes = 'This is an EC2'

# Double quotes
double_quote = "This is an S3 bucket"

# Triple quotes for multi-line strings
multi_line = """
This is a Cloudformation template.
Which has multiple lines

"""
print(single_quotes)
print(double_quote)
print(multi_line)

# Exercise

# Create a single quoted string for an AWS region name

single_quotes = 'This is an AWS region: us-west-1'

# Create a double quoted string for an ec2 instance type

double_quote = "This is an AWS EC2 type: t4g.small"

# Create a multi line string for a simple IAM policy

multi_line = """
AWS IAM policy: AccessAnalyzerServiceRolePolicy
function: Allow Access Analyzer to analyze resource metadata
"""

# Print all three strings

print(single_quotes)
print(double_quote)
print(multi_line)

# Exercise

# Create a single quoted string for an AWS region name

aws_region = 'This is an AWS region: us-west-1'

# Create a double quoted string for an ec2 instance type

ec2_instance_type = "This is an AWS EC2 type: t4g.small"

# Create a multi line string for a simple IAM policy

iam_policy = """
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AccessAnalyzerServiceRolePolicy",
            "Effect": "Allow",
            "Action": ["s3:ListAllMyBuckets", "ec2:DescribeVpcs"],
            "Resource": "arn:aws:s3::example-bucket"
        }
    ]
}
"""

# Print all three strings

print(aws_region)
print(ec2_instance_type)
print(iam_policy)