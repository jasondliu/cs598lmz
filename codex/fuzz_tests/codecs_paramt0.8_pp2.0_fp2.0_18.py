import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))

def find_albums(driver, artist_url):
    albums = []

    driver.get(artist_url)
    
    album_containers = driver.find_elements_by_class_name("album-container")
    for album_container in album_containers:
        container_a = album_container.find_element_by_class_name("container-coverart")
        album_title = container_a.get_attribute("title")
        album_url = container_a.get_attribute("href")
        album_artwork = album_container.find_element_by_class_name("cover-art-image").get_attribute("src")
        albums.append((album_title, album_url, album_artwork))

    return albums

def find_songs(driver, album_url):
    songs = []

    driver.get(album_url)

    song_containers = driver.find_elements_by_class_name("song-container")
    for song_container in song
