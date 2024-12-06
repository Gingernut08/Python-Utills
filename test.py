import math

## cd my drive/a-levels/cs/cs nea

class projectile:
	def __init__(self, gravitationalConstant, dragCo, mass, initVelocity):
		self.gravitationalConstant = gravitationalConstant
		self.dragCo = dragCo
		self.mass = mass
		self.initVelocity = initVelocity

	def calc_range(self, theta, dt):
		xPoints = [0]
		yPoints = [0]
		xPosition = 0
		yPosition = 0

		theta = math.radians(theta)

		xVelocity = self.initVelocity * math.cos(theta)
		yVelocity = self.initVelocity * math.sin(theta)
		while yPosition >= 0:
			currentVelocity = math.sqrt(xVelocity**2 + yVelocity**2)

			xVelocity = xVelocity - (self.dragCo / self.mass) * currentVelocity * xVelocity * dt
			yVelocity = yVelocity - (self.gravitationalConstant + (self.dragCo / self.mass) * currentVelocity * yVelocity) * dt

			xPosition += xVelocity * dt
			yPosition += yVelocity * dt

			xPoints.append(xPosition)
			yPoints.append(yPosition)

		range_projectile = round(float(xPoints[-1]), 2)
		return range_projectile

	def calc_angle(self, target, dt):
		ranges = []
		for i in range(0, 45):
			ranges.append(self.calc_range(i, dt))

		return ranges




g = 9.81 
k = 0.128  
m = 0.145  
v_0 = 1000
dt = 0.01
theta = 45


test = projectile(g, k, m, v_0)

print(test.calc_angle(10, dt))


