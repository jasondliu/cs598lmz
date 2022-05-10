import bz2
bz2.open(p.filename.replace('.json.bz2', '.sw'), 'r', encoding='utf-8')

print('READER-URL:', p.reader_url)

df = p.read()
df

```

    TGT-DIR-PATH: /examples/example_data/search_wat
    READER-URL: https://unpkg.com/datasets-reader-twitter@0.3.0/dist/src/compaction/gzip_json_lines/main.js
    SKIPPED-ITEMS: 0
    SKIPPED-ITEMS: 0
    SKIPPED-ITEMS: 0
    SKIPPED-ITEMS: 0
    SKIPPED-ITEMS: 0



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</
