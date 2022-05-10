import sys, threading
threading.Thread(target=lambda: sys.__stdout__.write('Hello, world!')).start()
```

### Вставка в базу данных

```sql
insert into User
select 'test2' as name, 'test2' as password, 'test2' as email, 'test2' as sex, 'test2' as country, 'test2' as about
```

### Изменения в строках

```sql
update User
set password = 'Qwerty', email = 'test@test.ru'
where User.id = 1
```

```sql
update User
set password = 'Qwerty', email = 'test@test.ru'
where User.id = 1
```

### Удаление из таблицы

```sql
delete from User
where User.id = 2
```

### Выбор
