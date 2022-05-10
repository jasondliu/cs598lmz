import threading
threading.Thread(target=lambda: os.system('python -m http.server --cgi 8080')).start()
```

## `w3m`

```sh
#!/usr/bin/env bash

w3m -o display_image=true "$@"
```

## `xclip`

```sh
#!/usr/bin/env bash

xclip -selection clipboard "$@"
```

## `xclip-paste`

```sh
#!/usr/bin/env bash

xclip -selection clipboard -o
```

## `xclip-select`

```sh
#!/usr/bin/env bash

xclip -selection primary "$@"
```

## `xclip-select-paste`

```sh
#!/usr/bin/env bash

xclip -selection primary -o
```

## `xclip-select-url`

```sh
#!/usr/bin/env bash

xclip -selection primary -o -t TARGETS | grep -q text/
