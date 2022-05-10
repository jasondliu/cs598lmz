import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/new_post/', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if request.method == 'POST' and form.validate():
        title = form.title.data
        keywords = form.keywords.data
        content = form.content.data
        new_post = BlogPost(title, keywords, content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_post.html', form=form)

@app.route('/index/')
def index():
    posts = BlogPost.query.order_by(BlogPost.date.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('
