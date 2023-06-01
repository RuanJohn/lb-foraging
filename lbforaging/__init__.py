from gym.envs.registration import registry, register, make, spec
from itertools import product

sizes = range(5, 20)
players = range(2, 20)
foods = range(1, 10)
coop = [True, False]
partial_obs = [True, False]

# for s, p, f, c, po in product(sizes, players, foods, coop, partial_obs):
#     register(
#         id="Foraging{4}-{0}x{0}-{1}p-{2}f{3}-v2".format(s, p, f, "-coop" if c else "", "-2s" if po else ""),
#         entry_point="lbforaging.foraging:ForagingEnv",
#         kwargs={
#             "players": p,
#             "max_player_level": 2,
#             "field_size": (s, s),
#             "max_food": f,
#             "sight": 2 if po else s,
#             "max_episode_steps": 50,
#             "force_coop": c,
#             "grid_observation": False,
#         },
#     )

# Manually create Foraging experiments for scaling tests. 

# 2 player, 2 food, 5x5
register(
    id="Foraging-5x5-2p-2f-v2",
    entry_point="lbforaging.foraging:ForagingEnv",
    kwargs={
        "players": 2,
        "max_player_level": 2,
        "field_size": (5, 5),
        "max_food": 2,
        "sight": 5,
        "max_episode_steps": 50,
        "force_coop": False,
        "grid_observation": False,
    },
)

# 4 player, 4 food, 10x10
register(
    id="Foraging-10x10-4p-4f-v2",
    entry_point="lbforaging.foraging:ForagingEnv",
    kwargs={
        "players": 4,
        "max_player_level": 2,
        "field_size": (10, 10),
        "max_food": 4,
        "sight": 10,
        "max_episode_steps": 50,
        "force_coop": False,
        "grid_observation": False,
    },
)

# 10 player, 10 food, 15x15
register(
    id="Foraging-15x15-10p-10f-v2",
    entry_point="lbforaging.foraging:ForagingEnv",
    kwargs={
        "players": 10,
        "max_player_level": 2,
        "field_size": (15, 15),
        "max_food": 10,
        "sight": 15,
        "max_episode_steps": 50,
        "force_coop": False,
        "grid_observation": False,
    },
)

# 20 player, 20 food, 20x20
register(
    id="Foraging-20x20-20p-20f-v2",
    entry_point="lbforaging.foraging:ForagingEnv",
    kwargs={
        "players": 20,
        "max_player_level": 2,
        "field_size": (20, 20),
        "max_food": 20,
        "sight": 20,
        "max_episode_steps": 50,
        "force_coop": False,
        "grid_observation": False,
    },
)

# 50 player, 50 food, 25x25
register(
    id="Foraging-25x25-50p-50f-v2",
    entry_point="lbforaging.foraging:ForagingEnv",
    kwargs={
        "players": 50,
        "max_player_level": 2,
        "field_size": (25, 25),
        "max_food": 50,
        "sight": 25,
        "max_episode_steps": 50,
        "force_coop": False,
        "grid_observation": False,
    },
)