FROM ubuntu:20.04
LABEL maintainer="Kl1rik Git"
USER root
RUN mkdir Django_feedback_app
COPY Kl1rik_test_project/ Django_feedback_app 
COPY initdb.py .
COPY django_run.sh .

RUN apt-get  update

RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install nano
RUN apt-get -y install inetutils-ping 
RUN apt-get -y install iproute2
RUN pip install python-dotenv
RUN pip install django mysql-connector-python

RUN chmod +x django_run.sh
EXPOSE 8000
CMD ["./django_run.sh"]