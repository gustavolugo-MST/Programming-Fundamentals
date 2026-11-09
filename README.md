# Programming Fundamentals: Python for Cloud Automation

Week 9 of my cloud engineering program. Small Python scripts that practice core fundamentals using AWS-shaped data (EC2 instance IDs, S3 bucket names, availability zones) instead of toy examples.

## The problem

Picture a company managing 500 rental properties in one database. Checking each one by hand is slow and error-prone. Now swap the properties for 500 AWS resources: EC2 instances, S3 buckets, RDS databases. Same problem.

Anyone running more than a handful of things in the cloud hits this. Python is how you stop doing it by hand.

## What I built

A set of small scripts, one per fundamental. Each uses cloud-flavored data so the practice carries over to real work.

| File | Concept | AWS-style example |
| --- | --- | --- |
| `hello_world.py`, `comments.py`, `indentation.py` | Basics, comments, indentation | n/a |
| `vars.py`, `strings.py`, `string_con.py` | Variables, strings, concatenation | Resource names |
| `lists.py` | Lists | EC2 instance IDs (add / remove) |
| `dictionary.py` | Dictionaries | One EC2 instance's details |
| `forloops.py`, `while_loops.py` | Loops | Checking every instance |
| `control_structures.py` | if / elif / else | Running vs stopped, public access block |
| `functions.py` | Functions | Unique S3 bucket name generator |

## The decisions

- **Fundamentals before Boto3.** I could have jumped straight into automating AWS. I chose to learn the building blocks first, so I can debug the code when it breaks.
- **AWS-shaped examples over toy ones.** Instance IDs and bucket names instead of fruit and cars. Slower to set up, but every exercise doubles as job practice.

## What broke

Using `=` instead of `==` in a condition:

```python
if instance_running = "running":   # SyntaxError
```

Python's error even suggested the fix. `=` assigns a value, `==` compares two values. The lesson: read the error message instead of guessing.

## The result

I can read and write the Python behind a simple AWS check. For example, `functions.py` generates a bucket name with a random 4-digit suffix (9,000 possible values per project name), which matters because S3 bucket names must be globally unique.

```python
import random

def generate_bucket_name(project_name):
    random_suffix = random.randint(1000, 9999)
    return f"{project_name}-bucket-{random_suffix}"
```

## Run it

```bash
python3 control_structures.py
```

## What's next

Boto3, the AWS SDK for Python, so this code can check real AWS resources.
