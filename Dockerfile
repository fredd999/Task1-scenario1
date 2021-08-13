# Docker Container - Builds container with centos7, python 3.8.6, ansible 2.10.7, and oter pkgs
#
# Edited April 02, 2021
#
# Container Image Size - 2.1GB
#
# Docker Build Command
# docker build . --network=host -t nexusrepo.clab.local/cent7-py38-dev:040221 
#
# Docker Run Command Example
# docker run --rm -v ${PWD}:/app nexusrepo.clab.local/cent7-py38-dev:040221 ansible-playbook <playbookfile.yml>

FROM centos/python-38-centos7:20210330-4d85c35

LABEL maintainer="gtamilse@cisco.com"
LABEL build_date="2021-04-02"
LABEL version="040221"

#Need to be root user to update centos pkgs
USER root

# Update centos pkgs and clean up
RUN yum -y --enablerepo=extras install epel-release && \
    yum -y update && \
    yum clean all && \
    rm -rf /var/cache/yum/*

# Install required pkgs
RUN yum -y install wget git curl zip unzip tree

# Copy the pip requirements to the container
COPY . .

# # Switch to non-root user
USER default

# Install required python pkgs (ansible 2.10.7 installed)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install  --no-cache-dir -r requirements.txt

# # Create cisco user noninteractively and set bash as default shell
# RUN useradd -ms /bin/bash cisco
# # Switch to non-root user Cisco
# USER cisco

# # Set home dir of user as workdir
# WORKDIR /home/cisco
WORKDIR /app

# Provide bash shell as entry point to container
ENTRYPOINT /bin/bash
