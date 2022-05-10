from lzma import LZMADecompressor
LZMADecompressor().decompress(extract_tarfile(tar_file, tar_file_name))
```

## Development
Development and testing of this project is managed with `poetry` (https://python-poetry.org/)

### Testing
```
./test.sh
```

### Publishing
```
poetry build
pip install dist/tarz.whl
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
