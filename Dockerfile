FROM python
WORKDIR /app
COPY . /app
EXPOSE 8080
CMD ["python3","main.py"]
