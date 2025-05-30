FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && \
    pip install uv && \
    python -m uv pip install -r requirements.txt

EXPOSE 4000
CMD ["python", "app.py"]