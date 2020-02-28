import json





# img_dimensions = [{'width': 960, 'height': 540, 'depth': 3}]


# def edit_json():
#
#     with open("training_dataset.manifest", "r") as read_file:
#         data = json.load(read_file)
#         for item in data.values():
#             item['image_size'] = item.pop('size')
#             item['image_size'] = img_dimensions
#             # item['bounding-box'] = img_dimensions
#             item['source-ref'] = "s3 bucket location"
#             for region in item['regions']:
#                 region['class_id'] = region.pop('name')
#                 region['left'] = region.pop('x')
#                 region['top'] = region.pop('y')
#
#             item['annotations'] = item.pop('regions')
#
#     with open('new.json', 'w') as outfile:
#         #print("data is there: ", data)
#         json.dump(data, outfile, indent=2)
#
#     #print(json.dumps(data))


# import boto3
#
# def create_project(project_name):
#
#     client=boto3.client('rekognition')
#
#     #Create a project
#     print('Creating project:' + project_name)
#     response=client.describe_projects()
#     print(response)
#     print('Done...')
#
# def main():
#     project_name='project'
#     create_project(project_name)

# if __name__ == "__main__":
#     edit_json()
