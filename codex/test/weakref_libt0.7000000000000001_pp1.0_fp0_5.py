import weakref

from tp.server.model import Model
from tp.server.rules.types import TypeClass
from tp.server.rules.units import UnitClass
from tp.server.rules.orders import OrderClass

class Orders(Model):
	"""
	The Orders table.
	"""
	__tablename__ = 'orders'

	id		= Column(Integer, primary_key=True)
	unit		= Column(Integer, ForeignKey('objects.id'), index=True)
	parent		= Column(Integer, ForeignKey('orders.id'), index=True)
	type		= Column(Integer, ForeignKey('order_types.id'), index=True)
	arguments	= Column(Text)

	on_insert = []
	on_update = []
	on_delete = []

class OrderTypes(TypeClass):
	"""
	OrderTypes table.
	"""
	__tablename__ = 'order_types'

	id		= Column(Integer, primary_key=True)
