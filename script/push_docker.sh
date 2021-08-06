#!/bin/sh

# Copyright 2021 Adevinta

# This script tags and pushes a locally existent docker image to a specified new
# tag. It receives two parameters, the first one specifies the tag of the local
# image and the second one the tag to push the image to. It expects the env
# variables: DOCKER_USERNAME and DOCKER_PASSWORD to be set. Those credentials
# must belong to a valid user with permission to push to the docker image
# registry the script will push the image to.

set -eu
if [ -z "$1" ]
  then
    echo "no local image tag specified"
fi

if [ -z "$2" ]
  then
    echo "no image tag to push to specified"
fi

LOCAL_TAG=$1
PUSH_TAG=$2
docker tag $LOCAL_TAG $PUSH_TAG
echo ${DOCKER_PASSWORD} | docker login -u $DOCKER_USERNAME --password-stdin
echo "pushing image to repository ${PUSH_TAG}"
docker push $PUSH_TAG
docker logout
