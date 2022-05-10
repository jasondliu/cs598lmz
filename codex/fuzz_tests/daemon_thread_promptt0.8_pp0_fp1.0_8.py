import threading
# Test threading daemon, add more threading if needed.
# threading.Thread(target=instagram.repost, args=(input_tag,input_name)).start()
threading.Thread(target=instagram.like, args=(input_tag,)).start()
threading.Thread(target=instagram.comment, args=(input_tag,input_com)).start()
threading.Thread(target=instagram.comment_tag, args=(input_tag,)).start()

```
## Credits

- [Edi Wibowo](https://github.com/edi-nasa12)

## License

[MIT](https://github.com/edi-nasa12/igtools/blob/master/LICENSE)
