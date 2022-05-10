import threading
threading.Thread(target=start_server, daemon=True).start()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/audio', methods=['GET'])
def audio():
    return render_template('audio.html')

@app.route('/video', methods=['GET'])
def video():
    return render_template('video.html')

# @app.route('/test', methods=['GET'])
# def test():
#     return render_template('test.html')

@app.route('/video_feed', methods=['GET'])
def video_feed():

    title = request.args.get('title')
    ext = request.args.get('ext').lower()
    print(title, ext)
    if not title:
        return 'Needs the title param', 400

    if ext not in ['mp4', 'avi']:
        return 'Extension must be mp4 or avi', 400

    # return Response(gen(VideoCamera
