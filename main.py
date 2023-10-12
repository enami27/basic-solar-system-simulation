import pygame
import math
pygame.init()

WIDTH, HEIGHT =  800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

WHITE = (255, 255, 255)
YELLOW = (255, 204, 82)
BLUE = (82, 163, 255)
RED = (225, 48, 21)
DARK_GREY = (74, 74, 72)

FONT = pygame.font.SysFont("monospace", 14)

class Planet:
	AU = 149.6e6 * 1000
	G = 6.67428e-11
	SCALE = 250 / AU  # 1AU = 100 pixels
	TIMESTEP = 3600*24 # 1 day

	def __init__(self, x, y, radius, color, mass):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.mass = mass

		self.orbit = []
		self.sun = False
		self.distanceToSun = 0

		self.XVel = 0
		self.YVel = 0

	def draw(self, win):
		x = self.x * self.SCALE + WIDTH / 2
		y = self.y * self.SCALE + HEIGHT / 2

		if len(self.orbit) > 2:
			updatedPoints = []
			for point in self.orbit:
				x, y = point
				x = x * self.SCALE + WIDTH / 2
				y = y * self.SCALE + HEIGHT / 2
				updatedPoints.append((x, y))

			pygame.draw.lines(win, self.color, False, updatedPoints, 2)

		pygame.draw.circle(win, self.color, (x, y), self.radius)
		
		if not self.sun:
			distanceText = FONT.render(f"{round(self.distanceToSun/1000, 1)}km", 1, WHITE)
			win.blit(distanceText, (x - distanceText.get_width()/2, y - distanceText.get_height()/2))

	def attraction(self, other):
		other_x, other_y = other.x, other.y
		distanceX = other_x - self.x
		distanceY = other_y - self.y
		distance = math.sqrt(distanceX ** 2 + distanceY ** 2)

		if other.sun:
			self.distanceToSun = distance

		force = self.G * self.mass * other.mass / distance**2
		theta = math.atan2(distanceY, distanceX)
		force_x = math.cos(theta) * force
		force_y = math.sin(theta) * force
		return force_x, force_y

	def update_position(self, planets):
		totalFX = totalFY = 0
		for planet in planets:
			if self == planet:
				continue

			fx, fy = self.attraction(planet)
			totalFX += fx
			totalFY += fy

		self.XVel += totalFX / self.mass * self.TIMESTEP
		self.YVel += totalFY / self.mass * self.TIMESTEP

		self.x += self.XVel * self.TIMESTEP
		self.y += self.YVel * self.TIMESTEP
		self.orbit.append((self.x, self.y))


def main():
	run = True
	clock = pygame.time.Clock()

	sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
	sun.sun = True

	earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
	earth.YVel = 29.783 * 1000 

	mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
	mars.YVel = 24.077 * 1000
	
	mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
	mercury.YVel = -47.4 * 1000

	venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
	venus.YVel = -35.02 * 1000
	
	planets = [sun, earth, mars, mercury, venus]

	while run:
		clock.tick(60)
		WIN.fill((17, 17, 17))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		for planet in planets:
			planet.update_position(planets)
			planet.draw(WIN)

		pygame.display.update()

	pygame.quit()


main()
