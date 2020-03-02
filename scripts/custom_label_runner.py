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
    # project_name = 'custom-labels-05'
    # project_arn = create_project(project_name)
    project_arn = 'arn:aws:rekognition:us-east-1:018632230441:project/custom-labels-05/1582930535021'
    version_name = '2.0'

    output_config = json.loads('{"S3Bucket": "pandvike-custom-label-output", "S3KeyPrefix": "2802"}')
    training_dataset = json.loads(
        '{"Assets": [{ "GroundTruthManifest": { "S3Object": { "Bucket": "pandvike-custom-label-training-dataset", "Name": "training_dataset.manifest" } } } ] }')
    # testing_dataset = json.loads('{"AutoCreate":true}')

    testing_dataset = json.loads(
        '{"Assets": [{ "GroundTruthManifest": { "S3Object": { "Bucket": "pandvike-custom-label-testing-dataset", "Name": "testing_dataset.manifest" } } } ]}')

    train_model(project_arn, version_name, output_config, training_dataset, testing_dataset)


if __name__ == "__main__":
    main()
