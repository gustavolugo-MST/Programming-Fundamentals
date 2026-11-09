import random

# def generate_bucket_name(project_name):
#     random_suffix = random.randint(1000, 9999)
#     bucket_name = f"{project_name}-bucket-{random_suffix}"
#     return bucket_name

# # Using the function
# new_bucket = generate_bucket_name("banana")
# print(f"Created new S3 bucket: {new_bucket}")

def generate_random_password(unique_password):
    random_suffix = random.randint(1000, 9999)
    password = f"{unique_password}-key-{random_suffix}"
    return password

# Using the function
new_bucket = generate_random_password("apple")
print(f"Created new passord: {new_bucket}")