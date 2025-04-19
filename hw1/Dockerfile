FROM scratch

COPY --from=python:alpine /usr/local/bin/python /usr/local/bin/python

COPY --from=python:alpine /usr/local/lib/python3.13 /usr/local/lib/python3.13

COPY --from=python:alpine /lib/ld-musl-x86_64.so.1 /lib/ld-musl-x86_64.so.1
COPY --from=python:alpine /usr/local/lib/libpython3.13.so.1.0 /usr/local/lib/libpython3.13.so.1.0
COPY --from=python:alpine /usr/lib/libz.so.1 /usr/lib/libz.so.1

COPY app.py /app.py

ENTRYPOINT ["/usr/local/bin/python", "/app.py"]