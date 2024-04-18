from stable_baselines3.common.env_checker import check_env
from ball_balance_env import BallBalanceEnv
from stable_baselines3 import SAC


# initialize your enviroment
env = BallBalanceEnv(render_mode="rgb_array")
# it will check your custom environment and output additional warnings if needed
check_env(env)
# learning with tensorboard logging and saving model
model = SAC("MlpPolicy", env, verbose=1, tensorboard_log="./sac_ball_balance_tensorboard/")
model.learn(total_timesteps=150000, log_interval=4)
model.save("sac_ball_balance")

