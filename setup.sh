#!/bin/bash

HOST=ec2-user@klaro.xyz

ssh -T $HOST << EOF
  # Stop locale complaints when logging in next time
  sudo sh -c 'echo -e "LANG=en_US.utf-8\nLC_ALL=en_US.utf-8" > /etc/environment'

  # Install system deps
  sudo yum -y update
  sudo amazon-linux-extras install nginx1
  sudo yum -y install python3
  sudo pip3 install gunicorn

  sudo service nginx start
  sudo chkconfig nginx on
EOF
