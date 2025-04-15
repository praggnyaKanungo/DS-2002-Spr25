# this is my python script and this is for part 2

import boto3
import requests
import argparse

# i am using arguments
parser = argparse.ArgumentParser(description="This is for dowloading an image and uploading it to s3 on public and generating a url.")
parser.add_argument("url", help="Image URL to download")
parser.add_argument("bucket", help="Your S3 bucket name")
parser.add_argument("expiration", type=int, help="Expiration time for the presigned URL in seconds")
args = parser.parse_args()

# going to get all the variables here based on what you put int!
url = args.url
bucket_name = args.bucket
expires_in = args.expiration
object_name = url.split("/")[-1]

# First I am going to download the image
response = requests.get(url)
if response.status_code == 200:
    with open(object_name, "wb") as f:
        f.write(response.content)
    print(f"Here I am going to downloaded image by the following name: {object_name}")
else:
    print("Image downloading didn't work, you might want to check the image!")
    exit(1)

# Then I am going to upload with public read! 
s3 = boto3.client("s3", region_name="us-east-1")
try:
    s3.upload_file(
        Filename=object_name,
        Bucket=bucket_name,
        Key=object_name,
	ExtraArgs={
            'ACL': 'private',
            'ContentType': response.headers.get('Content-Type', 'image/jpeg'),
            'ContentDisposition': 'inline'
        }
    )
    print(f"The image was uploaded to s3 with publid read access")
except Exception as e:
    print("Upload didn't work, here's what I got:", e)
    exit(1)

# here is my predesgined url
try:
    presigned_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_name},
        ExpiresIn=expires_in
    )
    print("\nThis is the Presigned URL (expires in", expires_in, "seconds):")
    print(presigned_url)
except Exception as e:
    print("I was not able to generate the url:", e)

