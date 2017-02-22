import sys
import time

class ProgressBar(object):
	"""ProgressBar"""
	def __init__(self, progressname = 'Progress',total = 100, current = 0, flushfreq = 0.001):
		self.total = total
		self.current = current
		self.progressname = progressname
		self.flushfreq = flushfreq

	@property
	def percentage(self):
		return int(self.current * 100 // self.total)

	def __len__(self):
		return self.percentage // 2
		
	@property
	def content(self):
		return self.progressname + ':  [' + '#' * len(self) + '.' * (50 - len(self)) + ']  ' + str(self.percentage) + '%' +'\r'

	def show(self):
		sys.stdout.write(' ' * len(self.content) + '\r')
		sys.stdout.flush()
		sys.stdout.write(self.content)
		sys.stdout.flush()
		time.sleep(self.flushfreq)

	def present(self):
		print(self.content)

	def modify(self, newcurrent, newtotal):
		self.total = newtotal
		self.current = newcurrent

	def update(self, newcurrent):
		self.current = newcurrent
		self.show()

	def increase(self, increment = 1):
		self.current = self.current + increment
		self.show()

	def restart(self):
		self.current = 0
