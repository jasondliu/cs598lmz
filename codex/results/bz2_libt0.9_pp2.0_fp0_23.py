import bz2
bz2.BZ2Compressor()
</code>
, the site was embedded in an iframe, and the iframe's src param was the url of the site.
I have another question: if the malware enters my pc by a bzip2 vulnerability, what will the bzip2 vulnerability do?


A:

For the vulnerability specifically, see CVE-2016-6293. 
According to the Symantec link you provided, this vulnerability allowed the attackers to inject a remote control program and download a malicious executable file. A remote control program allows the attackers to control your computer remotely — essentially, this gives the attackers full control of your system and allows them to execute any arbitrary programs they wish, gather information from your system, use your system to attack other systems, and so on. 

