import gym

env = gym.make("FrozenLake-v0")

print(env.action_space)
print(env.observation_space)

score=0


for _ in range(1000):
    env.reset()
    for _ in range(100):
        obs, rew, done, info = env.step(env.action_space.sample())

        if done:
            score+= rew
            break

print(score)
print(score/1000)
