import lzma
lzma.decompress(data).decode('str-8')
```

```
发现xss和post提交
```

```
index.php
<?php
require_once "config.php";
if($maintenance)
{
    echo "<center><h1>We Are Maintenance Now.</h1></center>";
    exit;
}
if(!empty($_GET['page']))
{
    $page = $_GET['page'];
}
else
{
    $page = 'index';
}
require_once "controller/$page".".php";
?>
```
```
index.php?page=index
index.php
<?php
if(isset($_POST['username'])&&isset($_POST['password']))
{
    if($_POST['username']=='root'&&$_POST['password']=='flag')
    {
        setcookie('username', $_POST['username']);
        header('location:admin.php');
    }
}?>
