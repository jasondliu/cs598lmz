import socket
socket.if_indextoname(4)
</code>
On my machine this returns "Local Area Connection".  I needed to get the name of the active adapter, not just any adapter, so I matched this to the <code>netsh</code> command output:
<code>&gt;&gt;&gt; socket.if_indextoname(4) == "Local Area Connection"
True
</code>
Once I had the right number, it was easy to reimplement this in Perl:
<code>my $cmd = "netsh interface show interface";
my $current = "Local Area Connection";
my $index = 0;
open (IN, "$cmd |") or die "Can't list interfaces from netsh";
while (&lt;IN&gt;) {
    chomp;
    if (/^\s+\d+\s+:\s+(\w.*)/) {
        if ($1 eq $current) {
            last;
        }
        $index++;
    }
}
close (IN);

say $index;
</code>
I couldn't work out how to reliably get the shell command to return something in
