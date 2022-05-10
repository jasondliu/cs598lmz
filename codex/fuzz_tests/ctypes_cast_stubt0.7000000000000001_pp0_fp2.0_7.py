import ctypes
ctypes.cast(p, ctypes.py_object).value = "something new"
</code>
I am wondering how to do this in Java, I know that in Java there is ctypes.cast(p, ctypes.py_object).value = "something new"
The following is a sample of what I am looking for 
<code>import java.lang.*;
import java.util.*;
import java.io.*;

public class HelloWorld{

     public static void main(String []args){

         String value = "something"
         double a = 1;
         double b = 2;
         double c = 3;
         double d = 4;

         // pointer p is created to point to value
         //(value, a, b, c, and d) are all put in a tuple
         // pointer p is created to point to value
         //(value, a, b, c, and d) are all put in a tuple

         // pointer p is created to point to value
         //(value, a, b, c, and d) are all put in a tuple
         // pointer p is created to point to value
