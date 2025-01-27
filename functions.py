from utils.Point import Point
import math

class ObstacleDetection:
    @staticmethod
    def count_obstacles(yellow_robots):
        return len(yellow_robots)

    @staticmethod
    def is_obstacle_in_path(obstacle_pos, robot_pos, target_pos, threshold=0.3):
        robot_to_target = Point(target_pos.x - robot_pos.x, target_pos.y - robot_pos.y)
        robot_to_obstacle = Point(obstacle_pos.x - robot_pos.x, obstacle_pos.y - robot_pos.y)
        
        path_length = math.sqrt(robot_to_target.x**2 + robot_to_target.y**2)
        
        if path_length > 0:
            robot_to_target.x /= path_length
            robot_to_target.y /= path_length
            
        projection = (robot_to_obstacle.x * robot_to_target.x + 
                     robot_to_obstacle.y * robot_to_target.y)
        
        if projection < 0 or projection > path_length:
            return False
            
        perp_dist = abs(robot_to_obstacle.x * (-robot_to_target.y) + 
                       robot_to_obstacle.y * robot_to_target.x)
                       
        return perp_dist < threshold

    @staticmethod
    def get_obstacles_in_path(robot, targets, yellow_robots):
        if len(targets) == 0:
            return []
            
        robot_pos = Point(robot.x, robot.y)
        target_pos = targets[0]
        obstacles_in_path = []
        
        for obs in yellow_robots.values():
            obs_pos = Point(obs.x, obs.y)
            if ObstacleDetection.is_obstacle_in_path(obs_pos, robot_pos, target_pos):
                obstacles_in_path.append(obs)
                
        return obstacles_in_path