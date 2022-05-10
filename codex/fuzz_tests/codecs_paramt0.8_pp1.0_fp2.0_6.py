import codecs
codecs.register_error('html.decode', codecs.xmlcharrefreplace_errors)

# Read the cached data from the pickle file
# If the pickle file exists, read from it, otherwise run get_blog_posts
blog_data = get_blog_posts()

# Create a new static site
with static_site.create_site(
    output_path='public',
    template_path=['templates']
) as site:
    pass

# Loop through the blog posts and data and create the appropriate files
for blog_post in blog_data:
    # Create the blog post file
    with codecs.open(
        'content/{0}.html'.format(blog_post['slug']),
        'w',
        'utf-8'
    ) as blog_post_file:
        blog_post_file.write(render_template(
            'blog_post.html',
            blog_post=blog_post
        ))

    # Add the blog post to the page index
    page_index.add_page(blog_post['title'], blog_post['slug'
