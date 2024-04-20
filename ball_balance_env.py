import numpy as np
from gymnasium import utils
from gymnasium.envs.mujoco import MujocoEnv
from gymnasium.spaces import Box
import os


# you can completely modify this class for your MuJoCo environment by following the directions
class BallBalanceEnv(MujocoEnv, utils.EzPickle):
    metadata = {
        "render_modes": [
            "human",
            "rgb_array",
            "depth_array",
        ],
        "render_fps": 100,
    }

    # set default episode_len for truncate episodes
    def __init__(self, episode_len=500, **kwargs):
        utils.EzPickle.__init__(self, **kwargs)
        # change shape of observation to your observation space size
        observation_space = Box(low=-np.inf, high=np.inf, shape=(10,), dtype=np.float64)
        # load your MJCF model with env and choose frames count between actions
        MujocoEnv.__init__(
            self,
            os.path.abspath("assets/ball_balance.xml"),
            5,
            observation_space=observation_space,
            **kwargs
        )
        self.step_number = 0
        self.episode_len = episode_len

    # determine the reward depending on observation or other properties of the simulation
    def step(self, a):
        reward = 1.0
        self.do_simulation(a, self.frame_skip)
        self.step_number += 1

        obs = self._get_obs()
        done = bool(not np.isfinite(obs).all() or (obs[2] < 0))
        truncated = self.step_number > self.episode_len
        return obs, reward, done, truncated, {}

    # define what should happen when the model is reset (at the beginning of each episode)
    def reset_model(self):
        self.step_number = 0

        # for example, noise is added to positions and velocities
        qpos = self.init_qpos + self.np_random.uniform(
            size=self.model.nq, low=-0.01, high=0.01
        )
        qvel = self.init_qvel + self.np_random.uniform(
            size=self.model.nv, low=-0.01, high=0.01
        )
        self.set_state(qpos, qvel)
        return self._get_obs()

    # determine what should be added to the observation
    # for example, the velocities and positions of various joints can be obtained through their names, as stated here
    def _get_obs(self):
        obs = np.concatenate((np.array(self.data.joint("ball").qpos[:3]),
                              np.array(self.data.joint("ball").qvel[:3]),
                              np.array(self.data.joint("rotate_x").qpos),
                              np.array(self.data.joint("rotate_x").qvel),
                              np.array(self.data.joint("rotate_y").qpos),
                              np.array(self.data.joint("rotate_y").qvel)), axis=0)
        return obs
