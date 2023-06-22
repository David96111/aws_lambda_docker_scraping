FROM python:3.9 as stage
 
RUN apt-get clean && apt-get update -y && apt-get install sudo unzip -y
ENV CHROMIUM_VERSION=1002910  
COPY install-browser.sh /tmp/
RUN /usr/bin/bash /tmp/install-browser.sh

FROM python:3.9 as base

COPY . /app
WORKDIR /app

RUN apt-get clean &&  apt-get update -y && apt-get install $(cat /tmp/chrome-deps.txt) -y

# Install Python dependencies for function
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY --from=stage /opt/chrome /opt/chrome
COPY --from=stage /opt/chromedriver /opt/chromedriver 
 
CMD ["python3","main.py","test"]