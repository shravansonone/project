FROM python
MAINTAINER  SHRAVAN SONONE
RUN mkdir /app
WORKDIR /app/
ADD ./flaskapp_docker /app/
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip3 install flask
RUN pip3 install flask-mysqldb
RUN pip3 install mysql-connector-python
RUN pip3 install pyyaml
EXPOSE 9000
ENTRYPOINT [ "python3" ]
CMD [ "webapp.py" ]
