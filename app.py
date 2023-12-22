from flask import Flask , request, render_templates

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def calculator():
    data=request.form.get('data')
    if data:
        data=[float(num)]
        area=length*breadth
    else:
        area=None
    
    return render_templates("index.html")

if __name__=='__main__':
    app.run(debug=True)