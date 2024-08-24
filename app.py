import requests
from wsgiref.simple_server import make_server

def application(environ, start_response):
    if environ['PATH_INFO'] == '/':
        # Возвращаем HTML-страницу
        status = '200 OK'
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)
        with open('index.html', 'r') as file:
            return [file.read().encode('utf-8')]

    elif environ['PATH_INFO'] == '/getSettings':
        url = "https://1103.api.green-api.com/waInstance1103106013/getSettings/9a1426b6a27040ddb4ef1e93e6f287ec7ef6235b0b634c1bb2"
        response = requests.get(url)
        
        status = '200 OK'
        headers = [('Content-type', 'application/json')]
        start_response(status, headers)
        return [response.text.encode('utf-8')]
    
    elif environ['PATH_INFO'] == '/getStateInstance':
        url = "https://1103.api.green-api.com/waInstance1103106013/getStateInstance/9a1426b6a27040ddb4ef1e93e6f287ec7ef6235b0b634c1bb2"
        response = requests.get(url)
        
        status = '200 OK'
        headers = [('Content-type', 'application/json')]
        start_response(status, headers)
        return [response.text.encode('utf-8')]
    
    else:
        status = '404 Not Found'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return [b'Not Found']

if __name__ == '__main__':
    server = make_server('', 8051, application)
    print("Serving on port 8051...")
    server.serve_forever()

