# AWS Security Scripts

This repository contains Python scripts using the boto3 library to check and manage AWS resources' security settings.

## Scripts

### 1. Check S3 Buckets for Public Access and Remove It
- **File:** `scripts/check_s3_public_access.py`
- **Description:** This script checks if the S3 buckets have public access, and if so, removes it to avoid undesired access.

### 2. Check RDS Instances for Public Access and Remove It
- **File:** `scripts/check_rds_public_access.py`
- **Description:** This script checks if the RDS instances have public access, and if so, removes it to avoid undesired access.

### 3. Check EC2 Instances for SSM Policy and Remove It
- **File:** `scripts/check_ec2_ssm_policy.py`
- **Description:** This script checks if the EC2 instances have the SSM policy on their roles, and if so, removes that policy from all instances.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/aws_scripts.git
   cd aws_scripts

2. Create Virtual environment
    ```bash
    python3 -m venv aws

3. Activate virtual ennvironment aws
    ```bash
    source aws/bin/activate

4. Install dependencies 
    ```bash 
    cd disney_challange
    cd aws_scripts
    pip install -r requirements.txt

5. Usage:
    ```bash
    python scripts/check_s3_public_access.py
    python scripts/check_rds_public_access.py
    python scripts/check_ec2_ssm_policy.py

6. Test
    ```bash
    python -m unittest discover -s aws_scripts/tests




