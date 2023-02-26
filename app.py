 FROM ubuntu
 
 RUN apt-get update -y
 RUN apt-get install python3 -y
 RUN apt-get install python3-pip -y
 RUN apt-get clean all
 
 RUN pip install flask
  
 ADD app.py /tmp/app.py
 
 EXPOSE 80
 
 CMD ["python3" ,"/tmp/app.py"]
# docker
