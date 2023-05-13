from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def calculation():
        result = 0
        if request.method == 'POST':
                print(request.form.values)
                num_1, num_2 = request.form.get('first'), request.form.get('second')
                if request.form.get('sum'):
                        result = int(num_1) + int(num_2)
                        return render_template('front.html', result=result)
                if request.form.get('minus'):
                        result = int(num_1) - int(num_2)
                        return render_template('front.html', result=result)
                if request.form.get('division'):
                        result = int(num_1) / int(num_2)
                        return render_template('front.html', result=result)
                if request.form.get('multi'):
                        result = int(num_1) * int(num_2)
                        return render_template('front.html', result=result)
        result = 0
        return render_template('front.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)