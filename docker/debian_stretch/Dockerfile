FROM debian:stretch-slim
MAINTAINER harsha69

# Project Informations.
LABEL name ahsrah
LABEL src "https://github.com/upadrastaharshavardhan/ahsrah"
LABEL creator anouarbensaad
LABEL desc "ahsrah is a cms and vulnerabilites detection, an intelligent auto shell injector,\
            fast cms detection of target and fast scanner and informations gathering like\
	    subdomains, \
	    ipaddresses,\
	    country,    \
	    org,        \
	    timezone,   \
	    region,     \
	    ans         \
	    and more ...\
            Instead of injecting shell and checking it works like all the other tools do,\
            ahsrah analyses the response with and recieve if shell success uploaded or no.\
	    ahsrah is searching for urls with dorks."
	    
# Install Git,
RUN apt-get update -qq && \
    apt-get install -qq -y --no-install-recommends --no-install-suggests && \
        git        && \
	rm -rf /var/lib/apt/lists/* && \
    apt-get clean &&  \
    rm -rf /tmp/* /var/tmp/* /usr/share/doc/*

# Make ahsrah Directory & Clonning ahsrah From Github
RUN mkdir -p /usr/share/ahsrah && cd usr/share/ahsrah && \
    git clone https://www.github.com/upadrastaharshavardhan/ahsrah

# Make ahsrah group
RUN addgroup ahsrah

# added \\ahsrah [group] secondary group to ahsrah.
RUN adduser -G ahsrah -g "ahsrah user" -s /bin/sh -D ahsrah

# change ahsrah owner of directory of project.
RUN chown -R ahsrah ahsrah

# Switch user.
USER ahsrah

# Working−Directory
WORKDIR ahsrah

# Install Python3 & Pip 3
RUN apt-get update -qq && \
    apt-get install -qq -y --no-install-recommends \
        python3        \
        python3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean && \
    rm -rf /tmp/* /var/tmp/* /usr/share/doc/*

# Install Pip Packages.
RUN pip3 install requests && \
    pip3 install bs4

# Add Mount Volume Docker To Save All changes.
VOLUME [ "/ahsrah" ]

#run container with it mode & run python3 ahsrah.py -u ...
