import gym
import scipy

env = gym.make('FrozenLake-v0')

print(env.observation_space)

print(env.action_space)

score = 0
for _ in range(10000):
    env.reset()
    for t in range(100):
        obs, rew, done, info = env.step(env.action_space.sample())
        if done:
            score += rew
            break

print(score)