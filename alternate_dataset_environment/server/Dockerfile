FROM ubuntu:focal
ENV ELASTIC_VERSION=8.4.3

# Set Timezone
ENV TZ=Asia/Singapore
RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Package Installation
RUN apt-get update && apt-get install -y nginx vsftpd openssh-server libpcap0.8 curl

# Filebeat Installation
RUN curl -L -O -k https://artifacts.elastic.co/downloads/beats/packetbeat/packetbeat-${ELASTIC_VERSION}-amd64.deb && \ 
    dpkg -i packetbeat-${ELASTIC_VERSION}-amd64.deb && \ 
    rm packetbeat-${ELASTIC_VERSION}-amd64.deb

COPY packetbeat.yml /etc/packetbeat/packetbeat.yml
COPY services.sh /bin/services.sh
COPY vsftpd.conf /etc/vsftpd.conf

RUN chmod go-w /etc/packetbeat/packetbeat.yml
RUN chmod +x /bin/services.sh