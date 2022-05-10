import threading
threading.stack_size(64*1024)

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)
    socketio.init_app(app)
    with app.app_context():
        db.create_all()
    return app
