import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import launcher
launcher.run()
```

## Distribute :white_circle:

```bash
pyinstaller main.py --clean --onefile --noconsole -n "my_app" --add-data "data/*:data" --hidden-import="pkg_resources.py2_warn"
```

## Credits

- [Kivy](https://kivy.org) :white_check_mark:
