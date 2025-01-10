from aws_cdk import Stack
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as apigateway
from constructs import Construct

class PythonLambdaAppStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define Lambda Function
        my_lambda = _lambda.Function(
            self, 'MyPythonLambda',
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler='app.handler',  # File name and function
            code=_lambda.Code.from_asset('lambda')  # Path to the lambda code directory
        )

        # Optional: Add API Gateway to trigger Lambda
        apigateway.LambdaRestApi(
            self, 'MyApiEndpoint',
            handler=my_lambda
        )
