FROM balenalib/raspberry-pi:latest

RUN install_packages python3 python3-pip

COPY requirements.txt /root/nightvision/requirements.txt
RUN pip3 install -r /root/nightvision/requirements.txt
COPY __main__.py /root/nightvision/__main__.py

WORKDIR /root/nightvision
CMD python3 __main__.py
