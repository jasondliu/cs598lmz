import socket
socket.if_indextoname(3)

res = requests.get('https://api.ipify.org')

print(res.content)
</code>
So it appears that the <code>socket.if_indextoname</code> is returning the index of the interface, but how can I get this in the app?


A:

The <code>app.yaml</code> file that you provide to the <code>gcloud</code> tool allows you to configure instances by their role. You can set up different instances to do different jobs and they will be configured differently.
For your use case, you want to serve your requests on the <code>default</code> instance and you also want to run background tasks on a different, more powerful <code>worker</code> instance.
In the <code>gcloud</code> tool, you can configure the number of <code>worker</code> instances and the specifications of those instances; the <code>default</code> instances will always run on small, free machines. You might want to configure the <code>worker</code> instances to use a larger machine or to use a machine with a GPU, for example.
