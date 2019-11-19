FROM python:3.6

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
  && netdata

ENV PIP_FORMAT=legacy
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get install -y netcat && apt-get autoremove -y

# Create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

WORKDIR /faust/

COPY . /faust

ADD ./requirements.txt ./
RUN pip install -r requirements.txt

ENTRYPOINT ["./wait_for_services.sh"]