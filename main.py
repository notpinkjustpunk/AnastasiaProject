import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import imageio
import random
from matplotlib.animation import FuncAnimation

class DLA:
    def __init__(self, size=101):
        self.size = size
        self.matrix = np.zeros((size, size), dtype=bool)
        self.center = size // 2
        self.matrix[self.center, self.center] = True
        self.particles_added = 0
        self.frames = []

        if not os.path.exists('frames'):
            os.makedirs('frames')
        if not os.path.exists('media'):
            os.makedirs('media')

    def add_particle(self):
        x, y = self.get_random_edge_position()
        while True:
            x, y = self.random_walk(x, y)
            if self.has_neighbor(x, y):
                self.matrix[x, y] = True
                self.particles_added += 1
                self.capture_frame()
                break

    def get_random_edge_position(self):
        edge = random.choice(['top', 'bottom', 'left', 'right'])
        if edge == 'top':
            return random.randint(0, self.size-1), 0
        elif edge == 'bottom':
            return random.randint(0, self.size-1), self.size-1
        elif edge == 'left':
            return 0, random.randint(0, self.size-1)
        else:  # 'right'
            return self.size-1, random.randint(0, self.size-1)

    def random_walk(self, x, y):
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up' and y > 0:
            y -= 1
        elif direction == 'down' and y < self.size - 1:
            y += 1
        elif direction == 'left' and x > 0:
            x -= 1
        elif direction == 'right' and x < self.size - 1:
            x += 1
        return x, y

    def has_neighbor(self, x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size and self.matrix[nx, ny]:
                    return True
        return False

    def capture_frame(self):
        frame = self.matrix.copy()
        self.frames.append(frame)

    def create_gif(self):
        with imageio.get_writer('media/DLA.gif', mode='I') as writer:
            for frame in self.frames:
                plt.figure(figsize=(6, 6))
                sns.heatmap(frame, cbar=False, cmap='Blues', square=True)
                plt.axis('off')
                plt.savefig('temp_frame.png', bbox_inches='tight', pad_inches=0)
                plt.close()
                image = imageio.imread('temp_frame.png')
                writer.append_data(image)
        os.remove('temp_frame.png')

    def run(self, num_particles):
        for _ in range(num_particles):
            self.add_particle()
        self.create_gif()

    def animate(self, num_particles):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.axis('off')
        sns.heatmap(self.matrix, cbar=False, cmap='Blues', square=True, ax=ax)

        def update(frame):
            self.add_particle()
            ax.clear()
            sns.heatmap(self.matrix, cbar=False, cmap='Blues', square=True, ax=ax)
            ax.axis('off')

        anim = FuncAnimation(fig, update, frames=num_particles, repeat=False)
        plt.show()

if __name__ == "__main__":

    dla = DLA(size=301)
    dla.animate(num_particles=1000)