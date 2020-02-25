import json





img_dimensions = {'image_size': [{'width': 960, 'height': 540, 'depth': 3}]}


def edit_json():

    with open("formatted_json.json", "r") as read_file:
        data = json.load(read_file)
        for item in data.values():
            item['bounding-box'] = item.pop('size')
            item['bounding-box'] = img_dimensions
            item['source-ref'] = "s3 bucket location"
            for region in item['regions'].values():
                shape_attributes = region['shape_attributes']
                shape_attributes['class_id'] = shape_attributes.pop('name')
                shape_attributes['left'] = shape_attributes.pop('x')
                shape_attributes['top'] = shape_attributes.pop('y')

            item['annotations'] = item.pop('regions')

    with open('new.json', 'w') as outfile:
        print("data is there: ", data)
        json.dump(data, outfile, indent=2)


if __name__ == '__main__':
    data = edit_json()

