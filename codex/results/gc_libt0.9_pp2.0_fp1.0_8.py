import gc, weakref
from werkzeug.exceptions import NotFound

from loki.app.forms import PostForm, TagForm, SearchForm, CategoryForm
from loki.app.helpers import flash
from loki.app.models import User, Post, Tag, Category
from loki.app import helpers


bp = Blueprint("posts", __name__)


@bp.route("/posts", methods=["GET", "POST"])
@login_required
def show_posts():
    search = request.form.get("search")
    posts = g.current_user.posts.order_by(Post.created.desc())
    if search:
        posts = posts.filter(Post.title.like(f"%{search}%"))
        category_id = None
        tag_id = None
    else:
        category_id = request.form.get("category")
        tag_id = request.form.get("tag")
        if category_id != 'None':
            posts = posts.filter(Post.category_id == category_id)
            tag_id = None
        else
