# Dockerfile
FROM python:3.6

WORKDIR /usr/app

ADD ./requirements.txt ./
RUN pip install -r requirements.txt
RUN echo 'deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main' >> /etc/apt/sources.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends apt-utils \
  && curl -Ss 'https://raw.githubusercontent.com/netdata/netdata-demo-site/master/install-required-packages.sh' >/tmp/kickstart.sh \
  && bash /tmp/kickstart.sh -i netdata-all -y \
  && git clone https://github.com/netdata/netdata.git --depth=100 \
  && cd netdata \
  && ./netdata-installer.sh \
  && cd .. \
  && rm -Rf netdata \
  && netdata \
  && pip install -r requirements.txt

ADD ./ ./

CMD ["python", "app.py"]