FROM python:3-alpine
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
	    
# Clonning ahsrah From Github
RUN apk add --no-cache git && \
    git clone https://github.com/upadrastaharshavardhan/ahsrah.git

# Make ahsrah group
RUN addgroup ahsrah

# added \\ahsrah [group] secondary group to ahsrah.
RUN adduser -G ahsrah -g "ahsrah user" -s /bin/sh -D ahsrah

# change ahsrah owner of directory of project.
RUN chown -R ahsrah ahsrah

# Switch user.
USER ahsrah

ENV APP_HOME=ahsrah

# Working−Directory
WORKDIR $APP_HOME

# Install Pip Packages.
RUN pip install --user --upgrade pip && \
    pip install --user -r ./requirements.txt

# Add Mount Volume Docker To Save All changes. 
VOLUME [ "/ahsrah" ]

# Entrypoint -> Command : While Creating Container.
ENTRYPOINT [ "python", "ahsrah.py" ]

# Default Command When Starting The Container.
CMD ["--help"]
