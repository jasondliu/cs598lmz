import bz2
bz2.decompress(w2v_text[54:101] + b'\x00'*100)

```

```python
w2v_text[54:101]

```

```python
bz2.decompress(w2v_text[54:101])

```

```python
bz2.decompress(w2v_text[54:101] + b'\x00')

```

```python
with open(path.join('data', 'text8.bz2'), 'rb') as file:
    text = file.read()
len(text)

```

```python
w2v_text = spacy.load('en_vectors_web_lg')
w2v_text.vocab['google'].vector.shape

```

```python
w2v_text.vocab['google'].vector

```

```python
w2v_text.vocab['google'].vector.reshape(1, -1
