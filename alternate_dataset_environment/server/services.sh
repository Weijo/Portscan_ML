#!/bin/sh
#Start up script for metasploitable2 docker/gns3 image tleemcjr/metasploitable2

service ssh start
service vsftpd start
service nginx start
service packetbeat start

