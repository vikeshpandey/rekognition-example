import boto3

client = boto3.client('rekognition')
switch = {
    "1": "upload_from_s3",
    "2": "upload_from_local"
}


def upload_from_s3():
    print("detecting labels for file present in s3 bucket: ")
    print("enter the name of the s3 bucket(without s3 prefix): ")
    s3_bucket = input()
    print("enter name of the image present in s3 bucket: ")
    image_name = input()
    response = client.detect_labels(
        Image={'S3Object': {'Bucket': s3_bucket, 'Name': image_name}}, MaxLabels=10)

    detect_labels(response)


def upload_from_local():
    print("detecting labels for file present on local: ")
    print("enter name(with full path) of the image: ")
    image_name = input()
    with open(image_name, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    detect_labels(response)


def detect_labels(response):
    print('labels detected are: ')
    print()

    for label in response['Labels']:
        print('Label name: ' + label['Name'])
        print('Confidence score: ' + str(label['Confidence']))

        for instance in label['Instances']:
            print("Bounding boxes: ")
            print("Top: " + str(instance['BoundingBox']['Top']))
            print("Left: " + str(instance['BoundingBox']['Left']))
            print("Width: " + str(instance['BoundingBox']['Width']))
            print("Height: " + str(instance['BoundingBox']['Height']))
            print("Confidence: " + str(instance['Confidence']))

        print("Parents(if any): ")
        for parent in label['Parents']:
            print("   " + parent['Name'])
        print("----------")
        print()
    return len(response['Labels'])


def main():
    try:
        # photo='1057.jpg'
        # bucket='pandvike-custom-label-testing-dataset'
        print("Main Menu: ")
        print("\t1: detect labels for image uploaded from s3 bucket")
        print("\t2: detect labels for image uploaded from local")
        print("enter your choice: ")
        choice = input()
        func_to_call = switch.get(choice, "invalid choice")
        if func_to_call == "upload_from_local":
            upload_from_local()
        elif func_to_call == 'upload_from_s3':
            upload_from_s3()
    except Exception as e:
        print("Something went wrong, please check error logs:", e)


if __name__ == "__main__":
    main()
