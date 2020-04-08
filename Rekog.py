import image_helpers
import boto3


def rekog(link, vehicle):
    client = boto3.client('rekognition')
    name = ''

    imgbytes = image_helpers.get_image_from_url(link)

    rekresp = client.detect_labels(Image={'Bytes': imgbytes}
                                   , MinConfidence=0)
    for label in rekresp['Labels']:

        if label['Name'].lower() == vehicle.lower() or vehicle.lower() in label['Name'].lower():
            name = label['Name']
            return name.lower()



