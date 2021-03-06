from flask import Flask,url_for,render_template,request
from tfwrapper import imageRecognizer as ir
app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route('/upload',methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f=request.files['image']
        f.save('temp.jpg')
        results = ir.inferenceImage('temp.jpg')
        print(type(f))
        print(f)
      # results += human_string+": %.3f" % (score+0.0005) +'<br>'
        return render_template('result.html',results = results)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


# with app.test_request_context():
#   print ('====================',url_for('index'))
#   url_for('static', filename='style.css')

if __name__ == "__main__":
    app.run()
