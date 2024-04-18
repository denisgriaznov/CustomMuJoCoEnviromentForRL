from stable_baselines3 import SAC
from ball_balance_env import BallBalanceEnv
import cv2
import imageio

env = BallBalanceEnv(render_mode="rgb_array")
model = SAC.load("sac_ball_balance.zip")

obs, info = env.reset()
frames = []
for _ in range(500):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, truncated, info = env.step(action)
    image = env.render()
    if _ % 5 == 0:
        frames.append(image)
    cv2.imshow("image", image)
    cv2.waitKey(1)
    if done or truncated:
        obs, info = env.reset()

# uncomment to save result as gif
# with imageio.get_writer("media/test.gif", mode="I") as writer:
#     for idx, frame in enumerate(frames):
#         writer.append_data(frame)
