import types
types.new_class( "Login", (object,), { "loggedIn": False, "user": None })
</code>
I have 2 questions in this regard:
1) Is there a way to write the property so that I can access the user attribute without having to write <code>self.user</code> (basically, I would like to access <code>Login().user</code> like a global variable as opposed to an instance variable (using <code>self</code>).
2) Is there a way to write the property so that I can access the attribute <code>user</code> with <code>Login().user</code> and not <code>Login().user()</code> (i.e. the parenthesis should not be part of the syntax)


A:

I think you're over-thinking this. 
<blockquote>
<p>I would like to access Login().user like a global variable as opposed to an instance variable (using self).</p>
</blockquote>
You don't need a property for this. You can just define a class attribute:
<code>class Login(object):
    user
