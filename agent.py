from utils.ssl.Navigation import Navigation
from utils.ssl.base_agent import BaseAgent
from utils.Point import Point
from utils.Geometry import Geometry
import math

class ExampleAgent(BaseAgent):
    def __init__(self, id=0, yellow=False):
        super().__init__(id, yellow)
        self.max_velocity = 1.5  # Maximum velocity in m/s
        self.repulsion_strength = 100.0  # Strength of repulsion force
        self.obstacle_influence_range = 0.3  # Range in meters where repulsion is applied

    def decision(self):
        if len(self.targets) == 0:
            return

        target = self.targets[0]

        # Calculate attraction to the target
        target_velocity, target_angle_velocity = Navigation.goToPoint(self.robot, target)
        attraction = target_velocity

        # Calculate repulsion from obstacles
        repulsion = Point(0, 0)
        for robot_id, robot in self.opponents.items():
            if robot_id == self.id:
                continue  # Skip self
            obstacle_pos = Point(robot.x, robot.y)
            distance = self.pos.dist_to(obstacle_pos)
            if distance < self.obstacle_influence_range:
                direction = self.pos - obstacle_pos
                direction = direction.normalize()
                repel_force = direction * (self.repulsion_strength / (distance ** 2))
                repulsion += repel_force

        # Combine attraction and repulsion
        total_force = attraction + repulsion
        total_force = total_force.normalize() * self.max_velocity  # Normalize and scale to max velocity

        # Set the velocity and angular velocity
        self.set_vel(total_force)
        self.set_angle_vel(target_angle_velocity)  # Simple implementation, angular velocity can be adjusted based on need

        return

    def post_decision(self):
        pass