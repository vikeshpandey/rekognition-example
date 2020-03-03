# rekognition-examples

This repo contains examples of capabilities of rekognition. Following examples are available in this repo:

- detecting custom labels
- detecting random labels
- detecting faces with bounding boxes
- detecting labels in videos

##Detecting custom labels
for detecting custom labels, the following pre-requisites should be met:

- create three s3 buckets for containing training data, testing data and output of rekognition training job.
- ensure than rekognition has appropriate permissions on those s3 buckets. for details on how to set this up, please refer to: https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-sdk-bucket-permssions.html
- understand how the manifest file for custom label looks like. read: https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/cd-required-fields.html
- unzip the training_dataset.zip and upload the contents of it to the training bucket you created in first step.
- unzip the content of test_dataset.zip and upload the contents of it to the testing dataset bucket you created in first step.
