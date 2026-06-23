#/bin/bash

echo "Enter base64 encoded hash: "

read bash

echo $bash | base64 -d
