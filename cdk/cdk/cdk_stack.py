from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "exampleBucket",
            bucket_name="rossfirstbucket-fordev12"
        )
