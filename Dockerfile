FROM python:3
RUN git clone https://github.com/Oriel-Barroso/Final-20-05-21.git
RUN pip install pip
RUN pip install parameterized
WORKDIR /Final-20-05-21
CMD ["python3","-m","unittest"]