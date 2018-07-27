import gym
env = gym.make("FrozenLake-v0")

for _ in range(400):
    env.reset()
    obs, rew, done, info = env.step(0)
    env.render()
    print("observation is")
    print(obs)
    print("reward is")
    print(rew)
    print("done is")
    print(done)
    if done:
        break



print("action space is")
print(env.action_space)
env.render()

