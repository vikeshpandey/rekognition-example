# rekognition-examples

This repo contains examples of capabilities of rekognition. Following examples are available in this repo:

- detecting custom labels
- detecting random labels
- detecting faces with bounding boxes
- detecting labels in videos

##Detecting custom labels
for detecting custom labels, the following pre-requisites should be met:

- create three s3 buckets for containing training data, testing data and output of rekognition training job.
- ensure than rekognition has appropriate permissions on those s3 buckets. for details on how to set this up, please 
refer to: https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-sdk-bucket-permssions.html
- understand how the manifest file for custom label looks like. read: https://docs.aws.amazon.com/rekognition/latest/
customlabels-dg/cd-required-fields.html
- unzip the training_dataset.zip and upload the contents of it to the training bucket you created in first step.
- unzip the content of test_dataset.zip and upload the contents of it to the testing dataset bucket you created in first
 step.
- (Optional) change the region from us-east-1 to your choice of region, if you want to. you can find the region value in
 _**scripts/custom_labels/custom_label_runner.py**_

once all the above points are setup, run the **custom_label_runner.py** located under **scripts/custom_labels**. it will
 ask for a number of inputs like project name, version number, bucket locations etc. Once all the info is filled up 
 correctly, it will start the job. The training job might take around 30-40 minutes to complete. Once the job is complete, 
 just go back to the rekognition console, and you will see lot of information available regarding the model which has 
 just been training along with an endpoint which you can deploy to start using it.