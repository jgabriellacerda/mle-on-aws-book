#!/usr/bin/env bash

# Build the docker image

dockerfile_path=$1
tag=$2
image=$3

docker build \
-t "${image}:${tag}" \
-f ${dockerfile_path} . 
