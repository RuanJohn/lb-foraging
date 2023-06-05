from gym.envs.registration import registry, register, make, spec

# Manually create Foraging experiments for scaling tests. 

register(
    id="Foraging-15x15-3p-3f-det-max-food-sum-v2",
    entry_point="lbforaging.foraging:ForagingEnv",
    kwargs={
        "players": 3,
        "max_player_level": 2,
        "field_size": (15, 15),
        "max_food": 3,
        "sight": 15,
        "max_episode_steps": 50,
        "force_coop": False,
        "grid_observation": False,
        "sum_food_level": True, 
    },
)

register(
    id="Foraging-15x15-3p-3f-det-v2",
    entry_point="lbforaging.foraging:ForagingEnv",
    kwargs={
        "players": 3,
        "max_player_level": 2,
        "field_size": (15, 15),
        "max_food": 3,
        "sight": 15,
        "max_episode_steps": 50,
        "force_coop": False,
        "grid_observation": False,
        "sum_food_level": False, 
    },
)