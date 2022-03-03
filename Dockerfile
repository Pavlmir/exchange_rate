FROM python:3.8.6

RUN apt-get update
RUN pip3 install --upgrade pip

WORKDIR /code
COPY ./ /code/

RUN apt-get install -y golang
RUN apt-get install -y protobuf-compiler
RUN go get -u github.com/verloop/twirpy/protoc-gen-twirpy
ENV PATH=$PATH:/home/pavlmir/go/bin/

RUN pip3 install twirp
RUN pip3 install uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "3000"]
