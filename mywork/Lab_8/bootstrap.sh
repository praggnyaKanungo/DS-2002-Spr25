#!/bin/bash
apt update -y
apt upgrade -y
apt install -y git python3-pip
pip3 install boto3
