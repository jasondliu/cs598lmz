import socket
socket.if_indextoname(1)
</code>
Будет возвращать имя интерфейса по его индексу(в данном случае ethernet)
А функция if_indextoname
<code>if_indextoname(index) -&gt; string
</code>
Возвращает имя интерфейса, которому соответствует переданный индекс. Повтор имени может быть изменен в любое время. index должен бы
