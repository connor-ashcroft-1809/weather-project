FROM python:3.10

WORKDIR /streamlit-app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["streamlit", "run", "--server.port", "80", "app.py"]