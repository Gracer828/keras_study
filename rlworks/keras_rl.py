import gym

"""
カートは左右にしか動けません．なので，カートが取れる行動としては，右と左の2値です．
現在の環境に応じて，右か左か選択して，いい感じにバランスをとります．これは以下のように確認できます
"""
env = gym.make('CartPole-v0')
env.action_space
# Discrete(2)

env.action_space.sample()
# 0

# カートが得ることができる環境についての4つの値(カートの場所，カートの速度，ポールの角度，ポールが回転する速さ)
env.observation_space
# Box(4,)

env.observation_space.sample()
# array([  4.68609638e-01, 1.46450285e+38, 8.60908446e-02, 3.05459097e+37])