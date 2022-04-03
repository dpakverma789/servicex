# from django.contrib.auth.base_user import BaseUserManager
#
#
# class CustomerManager(BaseUserManager):
#     use_in_migrations = True
#
#     def create_user(self, contact, password=None, **other_fields):
#         if not contact:
#             raise ValueError('Contact is Required')
#         user = self.model(contact=contact, **other_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
