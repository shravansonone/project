FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_DATABASE flaskpp

ADD database.sql /docker-entrypoint-initdb.d/
EXPOSE 3306
