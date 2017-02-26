from bottle import get, run, static_file

@get('/')
def get_index():
    return static_file('index.html', root='.')

@get('/<filename:path>')
def get_static(filename):
    return static_file(filename, root='.')
    
if __name__ == "__main__":
    run(host='localhost', port=8080)