gi = (i for i in ())
# Test gi.gi_code.co_zombi
</code>
When this test is passed and <code>gi.gi_code.co_zombi</code> is still <code>False</code>, you can use <code>gi</code> as a sentinel for your tests. Use <code>gi is None</code> instead of <code>gi</code> itself to compare against something (but notice <code>gi is None</code> is <code>False</code> initially, and <code>gi is not None</code> after the generator completes).

