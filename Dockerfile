FROM python
RUN  pip install pipenv && \
        pipenv --python 3.7
RUN mkdir -p /app
COPY main.py /app
WORKDIR /app
RUN pip3 install requests
CMD ["python", "-m", "main"]
