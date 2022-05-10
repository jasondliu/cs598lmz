fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi()
sys.modules.clear()
sys.modules.update({'hashlib': hashlib, 'sys': sys})
hashlib.sha1 = fn
hash = hashlib.sha1()
print(hash.digest_size)
```

Flag: `watevr{fUcK_Y0u_y0u_CrAzY_A$h_FucK}`

## Reversing: Reversing (soso)

Блю Шелл с солингом

Ключ: `watevr{x64_R3v3R53}`

## Reversing: Reversing (dank)

ELF с симлинками

Ключ: `watevr{5L1CK_L1NK5}`

## Reversing: Reversing (crackme)

Кракме от Димы с услов
