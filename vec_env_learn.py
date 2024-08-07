from stable_baselines3.common.env_checker import check_env
from ball_balance_env import BallBalanceEnv
from stable_baselines3 import SAC
from stable_baselines3.common.env_util import make_vec_env

# initialize your enviroment
env = BallBalanceEnv(render_mode="rgb_array")
# it will check your custom environment and output additional warnings if needed
check_env(env)
# vectorized envs creating
vec_env = make_vec_env(BallBalanceEnv, n_envs=4)
model = SAC("MlpPolicy", vec_env, verbose=1, tensorboard_log="./sac_ball_balance_tensorboard/")
model.learn(total_timesteps=1500, log_interval=4)
model.save("sac_ball_balance")

