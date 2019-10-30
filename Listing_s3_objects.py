import boto3
import os

FILE_PATH = '/Volumes/GoogleDrive/Mi unidad/Operations/Reporting/Reporting_Repository/s3_list/list_s3.csv'
S3 = boto3.client('s3')
BUCKET = 'gjl-safebox'


def get_s3_keys(bucket):
    """Get a list of keys in an S3 bucket."""
    keys = []
    response = S3.list_objects_v2(Bucket=bucket)
    for obj in response['Contents']:
        keys.append(obj['Key'])
    return keys


def write_json(list_of_keys):
    my_data_file = open(FILE_PATH, 'w')
    column_title_row = "name\n"
    my_data_file.write(column_title_row)
    for key in list_of_keys:
        row = str(key + "\n")
        my_data_file.write(row)
    my_data_file.close()


os.remove(FILE_PATH)
print('get keys')
keys = get_s3_keys(BUCKET)
print('write file')
write_json(keys)


