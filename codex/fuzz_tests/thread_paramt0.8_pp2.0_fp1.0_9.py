import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join('Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1,101)))).start()

# using System.Linq
Enumerable.Range(1,100).Select(i => (i%3, i%5) match { case (0, 0) => "FizzBuzz" case (0, _) => "Fizz" case (_, 0) => "Buzz" case _ => i.ToString() }).Dump();

# using System.Linq
Enumerable.Range(1, 100).Select(i => i % 15 == 0 ? "FizzBuzz" : i % 3 == 0 ? "Fizz" : i % 5 == 0 ? "Buzz" : i.ToString()).Dump();
# using System.Linq
Enumerable.Range(1, 100).Select(i =>
  {
      if (i % 15 == 0)
          return "FizzBuzz";
      if (i % 3 == 0)
          return "Fizz";
      if (
