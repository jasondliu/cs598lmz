import lzma
lzma.decompress(urlopen("https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh").read()).decode('utf-8')

def install_miniconda(version: str='latest', url: str='https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh'):
    v = int(version) if version in ['2','3'] else 3
    vv = 'latest' if version in ['','latest'] else version
    return !bash -c "curl https://repo.continuum.io/miniconda/Miniconda3-{vv}-Linux-x86_64.sh -o miniconda.sh; bash miniconda.sh -bfp /usr/local/miniconda{v}; . /usr/local/miniconda{v}/etc/profile.d/conda.sh; conda update -qy conda; conda install -qy jupyterlab; conda clean -tipsy;"
