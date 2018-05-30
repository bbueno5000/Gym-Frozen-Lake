import gym.envs.registration as registration

registration.register(entry_point='gym_frozen_lake.envs:FrozenLakeEnv',
                      id='FrozenLake_bbueno5000-v0',
                      reward_threshold=1.0,
                      timestep_limit=1000)
