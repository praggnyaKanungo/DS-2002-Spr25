#!/bin/bash

# the three args we need
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <local-file> <bucket-name> <expiration-in-seconds>"
    exit 1
fi

# retriving those vars like we need them
FILE=$1
BUCKET=$2
EXPIRATION=$3

echo "First, we will upload $FILE to s3://$BUCKET/"
# uploading it using the below command
aws s3 cp "$FILE" "s3://$BUCKET/"

# going to handle the error in case here cuz thats  good pratice
if [ $? -ne 0 ]; then
    echo "Upload did not work actually, so you need to check your file path and bucket name!"
    exit 1
fi

# then here is the presigned URL
echo "This is your presigned URL (this is going to expire in $EXPIRATION seconds)..."
SIGNED_URL=$(aws s3 presign "s3://$BUCKET/$(basename $FILE)" --expires-in "$EXPIRATION")

# then here is going to be the link
echo "Use this link ASAP because it iwll expire in $EXPIRATION seconds!:"
echo "$SIGNED_URL"

