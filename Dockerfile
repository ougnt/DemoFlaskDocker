From	python
WORKDIR	/App
COPY	requirements.txt /App
RUN		pip install -r requirements.txt
COPY	. /App
CMD		python app.py
