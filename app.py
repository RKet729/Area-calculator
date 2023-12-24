from flask import Flask, request, render_template
app=Flask(__name__)


@app.route('/' , methods=['GET' , 'POST'])

def calculator():
    if request.method == 'POST':
        length=float(request.form.get('length'))
        breadth=float(request.form.get('breadth'))
        area= length * breadth
    else:
        length=breadth=area=None
    return render_template('index.html', length=length, breadth=breadth, area=area)
if __name__=='__main__':
    app.run(debug=True)