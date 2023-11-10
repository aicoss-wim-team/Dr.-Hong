from flask import Flask, request, render_template, send_from_directory, url_for, redirect
# chatGPT 라이브러리가 실제로 존재하지 않으므로 대체되었습니다. 적절한 라이브러리를 사용해주세요.
# import chatGPT
import tempfile
import os


app = Flask(__name__)

# 업로드된 파일을 저장할 디렉토리 설정
# 프로젝트의 루트 디렉토리를 찾아 절대 경로로 설정합니다.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')


@app.route('/', methods=['GET', "POST"])
def form():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    uploaded_file = request.files['image']
    print(uploaded_file)
    uploaded_file.save('static/uploads/uploaded_image.png')
    
    return render_template('upload.html')


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    # app.run(debug=True, host='172.16.2.75', port=5000)
    app.run(debug = True, port = 5004, threaded=True)
