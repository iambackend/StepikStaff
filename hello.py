def app(environ, start_response):
    """Simplest possible application object"""
    data = [environ['QUERY_STRING'].split('&')]
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain')
    ]
    start_response(status, response_headers)
    # WSGIRestrictStdout Off
    print(environ)
    return ['\r\n'.join(environ['QUERY_STRING'].split('&'))]