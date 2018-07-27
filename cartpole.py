import gym

env = gym.make("CartPole-v0")
env.reset()
for i in range (20):
    action= env.action_space.sample() #0 is left, 1 is right
    obs, rew, done, info = env.step(1)

    print('is the game over')
    print(done)
    print("observation space of our environment is")
    print(env.observation_space)
    print("position of cart is")
    print(obs[0])
    print("velocity of cart is")
    print(obs[1])
    print("angle of pole")
    print(obs[2])
    print("angle of pole")
    print(obs[3])
    print("reward")
    print(rew)
    score=+rew
    print("score is")
    print(score)

    env.render()