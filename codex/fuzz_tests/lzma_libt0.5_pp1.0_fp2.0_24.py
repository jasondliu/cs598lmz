import lzma
lzma.LZMAError:
  File "/home/spencer/anaconda3/envs/tf_gpu/lib/python3.8/site-packages/lzma.py", line 4, in &lt;module&gt;
    from _lzma import *
ModuleNotFoundError: No module named '_lzma'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/spencer/anaconda3/envs/tf_gpu/bin/tensorboard", line 10, in &lt;module&gt;
    sys.exit(run_main())
  File "/home/spencer/anaconda3/envs/tf_gpu/lib/python3.8/site-packages/tensorboard/main.py", line 97, in run_main
    app.run(tensorboard.main, flags_parser=tensorboard.configure)
  File "/home/spencer/anaconda3/envs/tf_gpu/lib/python3.8/site-packages/ab
