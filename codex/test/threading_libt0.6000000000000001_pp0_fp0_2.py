import threading
threading.stack_size(67108864)

def create_app():
    app = Flask(__name__, static_folder="build/static", template_folder="build")

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import cv
    app.register_blueprint(cv.bp)

    from . import cv_personal
    app.register_blueprint(cv_personal.bp)

    from . import cv_work
    app.register_blueprint(cv_work.bp)

    from . import cv_education
    app.register_blueprint(cv_education.bp)

    from . import cv_skill
    app.register_blueprint(cv_skill.bp)

    from . import cv_language
    app.register_blueprint(cv_language.bp)

    from . import cv_interest
    app.register_blueprint(cv_interest.bp)

    from . import cv_reference
    app.register_
