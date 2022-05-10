import threading
threading.Thread(target = torrent_status).start()
client.get_torrents()

@app.route('/')
def main():
    torrents = client.get_torrents()
    for torrent in torrents:
        print(torrent.name)
    return render_template('index.html', torrents=torrents)

@app.route('/add/<link>')
def add_link(link):
    client.download_from_link(link)
    torrents = client.get_torrents()
    return render_template('index.html', torrents=torrents)

@app.route('/pause/<infohash>')
def pause(infohash):
    client.pause(infohash)
    torrents = client.get_torrents()
    return render_template('index.html', torrents=torrents)

@app.route('/resume/<infohash>')
def resume(infohash):
    client.resume(infohash)
    torrents = client.get
