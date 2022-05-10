import mmap
from pathlib import Path


def main():
    import pdb;pdb.set_trace()
    # FIXME: retrieve user + pass from ENVS
    export = Path("/home/memnoc/inbox")
    users = [str(u) for u in Path("/users").iterdir() if u.is_dir() and not u.name.startswith(".")]
    PROFILE = "memnoc/GPG_PASS/profile"
    gpg_pass = subprocess.run(["pass", PROFILE], capture_output=True).stdout.decode().strip()

    for user in users:
        user_dir = Path(f"/users/{user}")
        c = imaplib.IMAP4_SSL("webmail.heritage.edu")
        c.login(user, gpg_pass)

        c.select("inbox", readonly=False)
        result, data = c.uid("search", None, "ALL")

