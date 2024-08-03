from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/",methods=['POST','GET'])
def start():
    n=0
    if request.method=='POST':
        if 'id' in request.form:
            n = int(request.form.get("id"))
    return render_template("index.html",n=n)
if __name__=="__main__":
    app.run()