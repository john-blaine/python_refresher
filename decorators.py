import functools

user = { 'username': 'jose', 'access_level': 'admin' }

def make_secure(func):
  # By using this imported decorator, we ensure that the function
    # that is being passed in keeps its __name__ and its documentation
  @functools.wraps(func)
  def secure_function(*args, **kwargs):
    if user['access_level'] == 'admin':
      return func(*args, **kwargs)
    else:
      return f'No admin permissions for {user["username"]}.'
  
  return secure_function

@make_secure
def get_admin_password(panel):
  if panel == 'admin':
    return '1234'
  elif panel == 'billing':
    return 'super_secure_password'

print(get_admin_password('billing'))
