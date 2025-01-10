import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_deploy.lambda_deploy_stack import LambdaDeployStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_deploy/lambda_deploy_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaDeployStack(app, "lambda-deploy")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
