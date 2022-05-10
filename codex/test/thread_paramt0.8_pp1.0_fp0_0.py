import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()
from botocore.exceptions import ClientError
import requests

# This is a script that creates a sage maker notebook instance and a sagemaker role
# based on the inputs that it gets from the user. It can either create a new role
# or use an existing role based on the user's choice.

# This function checks if a given AWS IAM role exists
def iam_role_exists(role_name):
    try:
        iam.get_role(RoleName=role_name)
    except ClientError:
        return False
    else:
        return True

# This function creates a new AWS IAM role if it doesn't already exist
