import lzma
lzma = lzma

from . import app

__all__ = ()

@app.route('/api/<plugin>/<path:path>', methods=('GET',))
async def api_get(request, plugin, path):
    req = await request.json
    path = path.rstrip('/')
    if req['method'] == 'list':
        if path:
            path += '/'
        return json(await plugin_db.list(plugin, path))
    if req['method'] == 'get':
        return json(await plugin_db.get(plugin, path))

@app.route('/api/<plugin>/<path:path>', methods=('POST',))
async def api_post(request, plugin, path):
    req = await request.json
    path = path.rstrip('/')
    if req['method'] == 'list':
        if path:
            path += '/'
        return json(await plugin_db.list(plugin, path))
    if req['method'] == 'get':
       
