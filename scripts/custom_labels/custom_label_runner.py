import json

import boto3


def create_project(project_name):
    client = boto3.client('rekognition', 'us-east-1')

    # Create a project
    print('Creating project:' + project_name)
    response = client.create_project(ProjectName=project_name)
    project_arn = response['ProjectArn']
    print('project created, ARN is: ' + project_arn)
    return project_arn


def train_model(project_arn, version_name, output_config, training_dataset, testing_dataset):
    client = boto3.client('rekognition', 'us-east-1')
    print('starting training version no: ' + version_name)

    try:
        response = client.create_project_version(
            ProjectArn=project_arn,
            VersionName=version_name,
            OutputConfig=output_config,
            TrainingData=training_dataset,
            TestingData=testing_dataset)
        print("response::::",response)
        project_version_training_completed_waiter = client.get_waiter('project_version_training_completed')
        project_version_training_completed_waiter.wait(ProjectArn=project_arn, VersionNames=[version_name])

        describe_response = client.describe_project_versions(ProjectArn=project_arn, VersionNames=[version_name])
        for model in describe_response['ProjectVersionDescriptions']:
            print("Status: " + model['Status'])
            print("Message: " + model['StatusMessage'])
    except Exception as e:
        print(e)

    print('Training completed...')


def main():

    # project_arn = 'arn:aws:rekognition:us-east-1:018632230441:project/custom-labels-05/1582930535021'
    # version_name = '3.0'
    print("enter a project name for the example: ")
    project_name = input()
    project_arn = create_project(project_name)

    print("enter a value for version for the example: ")
    version_name = input()

    print("enter the value for s3 bucket(without prefix) where the output will be stored: ")
    s3_output_bucket = input()

    print("enter the value for s3 bucket location(without prefix) containing training dataset: ")
    training_dataset_location = input()

    print("enter the name and path(if any subpath in bucket) for groundtruth manifest file for training bucket: ")
    training_manifest_file = input()

    print("enter the value for s3 bucket location(without prefix) containing testing dataset: ")
    testing_dataset_location = input()

    print("enter the name and path(if any subpath in bucket) for groundtruth manifest file for testing bucket: ")
    testing_manifest_file = input()


    output_config = json.loads('{"S3Bucket": "'+s3_output_bucket+'", "S3KeyPrefix": "out"}')
    training_dataset = json.loads(
        '{"Assets": [{ "GroundTruthManifest": { "S3Object": { "Bucket": "'+training_dataset_location+'", "Name": "'+training_manifest_file+'" } } } ] }')


    testing_dataset = json.loads(
        '{"Assets": [{ "GroundTruthManifest": { "S3Object": { "Bucket": "'+testing_dataset_location+'", "Name": "'+testing_manifest_file+'" } } } ]}')

    train_model(project_arn, version_name, output_config, training_dataset, testing_dataset)


if __name__ == "__main__":
    main()
