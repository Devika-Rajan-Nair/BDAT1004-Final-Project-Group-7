from flask import Flask,jsonify,request,render_template

app=Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/google-charts/line-chart')
def google_pie_chart():
    #return render_template('Liabilities.html')
    return render_template('line-chart.html')


if __name__=="__main__":
    app.run()


    