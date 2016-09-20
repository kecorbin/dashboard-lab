FROM ubuntu
MAINTAINER Kevin Corbin, kecorbin@cisco.com
RUN apt-get update
RUN apt-get -y install git python python-pip
# Get the latest version of toolkit, pypi trails I believe
WORKDIR /opt
RUN git clone https://github.com/datacenter/acitoolkit
WORKDIR acitoolkit
RUN python setup.py install
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["aci-dashboard-tutorial.py"]
