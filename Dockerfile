FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/start.py src/start.py
COPY data/ data/

CMD ["python", "./src/start.py"]
