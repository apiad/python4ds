FROM python:3.9

WORKDIR /src/

ADD requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY . /src/

CMD [ "streamlit", "python4ds/app.py" ]