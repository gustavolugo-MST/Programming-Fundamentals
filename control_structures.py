# # Control Structures / Control Flow
# instance_running = "stopped" 

# # If Statements
# if instance_running == "running":
#     print("The ec2 is running")
# elif instance_running == "stopped":
#     print("the ec2 is stopped....")
# else:
#     print("the ec2 instance is in an unexpected state")

# public_access_block = "banana"

# # Write the if statement
# if public_access_block == True:
#     print("The Public Access is locked down")

# elif public_access_block == False:
#     print("The public access block open")

# else:
#     print("The public acess block is in an unexpected state")

# Write statement for S3 Bucket
if public_access_block == True:
    print("The Public Access to s3 bucket is blocked")

else:
    print("The Public Access to s3 bucket is open")

