import io

import boto3
from PIL import Image, ImageDraw


def show_faces(bucket, photo):
    client = boto3.client('rekognition')

    s3_connection = boto3.resource('s3')
    s3_object = s3_connection.Object(bucket, photo)
    s3_response = s3_object.get()

    stream = io.BytesIO(s3_response['Body'].read())
    image = Image.open(stream)

    response = client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name': photo}}, Attributes=['ALL'])

    img_width, img_height = image.size
    draw = ImageDraw.Draw(image)
    print("Detected faces for " + photo)
    for faceDetail in response['FaceDetails']:
        print("The detected face has an age between" + str(faceDetail['AgeRange']['Low']) + " and " + str(
            faceDetail['AgeRange']['High']))

        bounding_box = faceDetail['BoundingBox']
        left = img_width * bounding_box['Left']
        width = img_width * bounding_box['Width']
        top = img_height * bounding_box['Top']
        height = img_height * bounding_box['Height']

        print("Left: % 5.0f" % left)
        print("Width: % 5.0f" % width)
        print("Top: % 5.0f" % top)
        print("Height: % 5.0f" % height)
        draw.rectangle([left,top, left + width, top + height], outline='#00d400')

    image.show()

def main():
    print("Enter the bucket name(without prefix): ")
    bucket = input()
    print("Enter the photo name: ")
    photo = input()
    show_faces(bucket, photo)


if __name__ == '__main__':
    main()
