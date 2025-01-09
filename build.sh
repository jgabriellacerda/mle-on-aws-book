#!/usr/bin/env bash

# Build the docker image

dockerfile_path=$1
tag=$2
image=$3
python_version=$4

docker build \
-t "${image}:${tag}" \
-f ${dockerfile_path} . \
--build-arg module_path=${module_path} \
--build-arg target_dir_name=${target_dir_name} \
--build-arg requirements_file_path=${requirements_file_path} \
--build-arg python_version=${python_version}
