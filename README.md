## How to create Gymnasium enviroment from your MuJoCo model?

This example shows how to create a simple custom MuJoCo model and train a reinforcement learning agent using the Gymnasium shell and algorithms from StableBaselines.

To reproduce the result you will need python packages [MuJoCo](https://mujoco.readthedocs.io/en/stable/python.html), [Gymnasium](https://gymnasium.farama.org/index.html) and [StableBaselines3](https://stable-baselines3.readthedocs.io/en/master/) with the appropriate versions:

```
pip install mujoco==3.1.4
pip install gymnasium==0.29.1
pip install stable-baselines3==2.3.0
```
## Results of custom model

A simple ball balancing environment was implemented as a starting point. The observation consisted of 10 values (position and speed for rotating the platform along two axes and moving the ball along three axes). Each step the agent received a reward of 1 until he fell off the platform or the episode ended (500 steps by default). The Soft Actor Critic algorithm learned an acceptable policy in 150,000 steps.


<img align="left" width="400" height="300" src="media/learning_curve.png"><img align="right" width="280" height="280" src="media/test.gif">
