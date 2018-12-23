import os,sys

from flask import Flask, request, render_template, send_from_directory
from classify_gender import funwithimage

__author__ = 'aditya'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    # target = os.path.join(APP_ROOT, 'static/')
    #print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    #else:
        #print("Couldn't create upload directory: {}".format(target))
    #print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        #print(upload)
        #print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        #print ("Accept incoming file:", filename)
        #print ("Save it to:", destination)
        upload.save(destination)
        name = name ="D:/Flask/Gender_classification/images/" + filename
        print(name , file=sys.stdout)
        filename="upload/"+filename
        label=funwithimage(str(name));
    return render_template("register.html", image_name=filename ,label=label)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(port=4555, debug=False)
