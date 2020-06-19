class Store:
  def __init__(self, name):
    self.name = name
  
  @classmethod
  def franchise(cls, store):
    return cls(f'{store.name} - franchise')

store = Store('Burger King')

franchise_store = Store.franchise(store)

print(franchise_store.name)
  