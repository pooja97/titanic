
from flask import Flask,request 

app=Flask(__name__)

@app.route('/api',method=['POST'])
def say_hello():
    data=response.get_json(force=True)
    name=data['name']
    return 'hello {0}'.format(name)

if __name__ == '__main__':
    app.run(port=10001,debug=True)
    
