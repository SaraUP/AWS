import boto3

project = "AWS"
cf = boto3.client("cloudformation")

with open('template.yaml', 'r') as file:
    template = file.read()

response = cf.create_stack(
    StackName=project,
    TemplateBody=template
)

print(response)