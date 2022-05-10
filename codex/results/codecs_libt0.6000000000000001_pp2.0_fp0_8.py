import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Invalid email address!"
        if len(postData["password"]) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_password"] = "Passwords do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_
