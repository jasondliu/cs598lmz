import lzma
lzma_compress = lzma.compress

def get_image_metadata(request, image_id):
    """Return metadata about an image in the form of a mapping."""
    # Creates a function that returns all the necessary data
    def fill_data():
        image = Image.objects.get(pk=image_id)
        if image.name is None:
            image.name = 'No name'
        image.namelen = len(image.name)
        image.tags = image.tag_string.split(' ')
        image.usernamelen = len(image.uploader.username)
        yield json.dumps({
            'image': image.id,
            'width': image.width,
            'height': image.height,
            'format': image.content_type,
            'namelen': image.namelen,
            'tags': image.tags,
            'name': image.name,
            'usernamelen': image.usernamelen,
            'uploaded': time.mktime(image.uploaded.tim
