import gymnasium as gym
import rsoccer_gym
from gymnasium.envs.registration import register
from utils.CLI import Difficulty
import pygame

register(
    id="VSS-Project",
    entry_point="vssenv:ExampleEnv"
)

register(
    id="SSL-Project",
    entry_point="sslenv:SSLExampleEnv"
)

env = gym.make("SSL-Project", difficulty=Difficulty(1)) #Just set the difficulty to 1

env.reset()

terminated = False
while not terminated:
    action = env.action_space.sample()
    next_state, reward, terminated, _, _ = env.step(action)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminated = True
            break

env.close()