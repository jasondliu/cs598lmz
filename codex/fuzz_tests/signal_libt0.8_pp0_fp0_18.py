import signal
signal.alarm(4)

# Input
name = input("")

# Check
if "Hack" in name:
    print("Good Job")
else:
    print("Try Again")
```

We used `nc` command to retrieve flag at the end:

```bash
nc 2018shell.picoctf.com 58414
```

We submitted `Hack` as input and got the flag.

Flag: `picoCTF{ALARM_alarm_alarm_82418638}`
