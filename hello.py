def app(environ, start_response):
    """Simplest possible application object"""
    data = [environ['QUERY_STRING'].split('&')]
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain')
    ]
    start_response(status, response_headers)
 #    f1=open('/home/box/web/outttttttt.txt', 'w+')
	# f1.write(environ)
	# f1.close()
    print(environ['QUERY_STRING'])
    return ['\r\n'.join(environ['QUERY_STRING'].split('&'))]