import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World!\n')).start()
```

## Эквивалентная последовательность

```python
{
  "type": "document",
  "content": [
    {
        "type": "paragraph",
        "content": [
          {
            "type": "text",
            "text": "Hello World!\n"
          }
        ]
    }
  ]
}
```

## Ассоциативный массив данных

```json
{
  "guid": "fa0e8c54-9e76-11e7-abc6-cec278b6b50a",
  "phone": "+7(921)926-92-34",
  "birthday": "1991-09-01",
  "address": {
    "building": "27",
   
