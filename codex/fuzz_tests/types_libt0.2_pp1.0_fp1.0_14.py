import types
types.MethodType(lambda self: self.get_absolute_url(), None)

#
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     activation_key = models.CharField(max_length=40, blank=True)
#     key_expires = models.DateTimeField(default=datetime.date.today())
#
#     def __str__(self):
#         return self.user.username
#
#     class Meta:
#         verbose_name_plural=u'User profiles'
#
#
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile, created = UserProfile.objects.get_or_create(user=instance)
#
# post_save.connect(create_user_profile, sender=User)
#
#
# def user_post_save(sender, instance, signal, *args, **kwargs):
#     """
#     Make sure the user object has a profile.
#     """

