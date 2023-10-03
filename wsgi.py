import io
...
request_data = 'some request body'.encode('utf-8') # bytes object
environ['wsgi.input'] = io.BytesIO(request_data)
