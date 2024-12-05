FROM bitnami/spark:3.5.3

USER root

RUN install_packages curl

RUN curl https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector/10.0.2/mongo-spark-connector-10.0.2.jar \
--output /opt/bitnami/spark/jars/mongo-spark-connector-10.0.2.jar

RUN install_packages nano

# WORKDIR /usr/app

# ADD ./pyspark ./

# RUN chmod +x ./pyspark && \
#     mv ./pyspark /opt/bitnami/spark/bin/pyspark

# ENV SPARK_MODE=master

# USER 1001

# CMD ["/bin/bash", "-c", "sleep infinity"]

# CMD ["/opt/spark/bin/pyspark", "--master" ,"spark://localhost:4045", \
#       "--packages", ${SPARK_CONNECTOR},\
#       "--conf", ${SPARK_URI_READ}]