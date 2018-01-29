from werkzeug.wrappers import Request, Response
from wakeonlan import wol
import json

@Request.application
def application(request):
    print (request.args, request.base_url, request.data, request.files)
    try:
        if request.path == '/json':
            data = request.data.decode('utf-8') 
            print('json', data)
            
            js = json.loads(data)
            print (js['command'])
            command = js['command']
            if command == 'wol':
                wol.send_magic_packet('90-2B-34-D5-EC-0E')
                return Response('OK\n')
            
            return Response('Unknown command "' + command + '"\n' )
    except:
        return Response('Error\n')
    
    return Response('Unknown request\n')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
