import threading
threading.stack_size(20000)

if __name__ == '__main__':
    flask_app = create_app()
    # app.run(port=5000, debug=True)
    flask_app.run(debug=True, threaded=True, host='0.0.0.0', port=5000)
    app.run()
