import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Extension Test\n')).start()`
[Extension Test](../../test/test.py)
```

New with PR # [#1](https://github.com/msoedov/CodePen-Collector/pull/1)

##### Script
To collect javascript code by selecting some text. 

```html
<script type="text/javascript">
    alert('Hello World!');
</script>
```

New with PR # [#1](https://github.com/msoedov/CodePen-Collector/pull/1)

## Todo

- [x] Version 2.1.0 - Run-count
- [x] Version 2.0.0 - Blank pen, etc. 
- [x] Version 0.1.0 - Fetches code by selecting it and pressing `Alt`+`C`
- [ ] Version 0.2.0 - Fetches code by selecting it and we can select what to collect in
  a menu?
- [ ] Version 0.3.0 - Settings page in extension
- [
