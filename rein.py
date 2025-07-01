import numpy as np
import random

road_length = 5 # Road will have 5 positions; 0, 1, 2, 3, 4
actions = ['left', 'right']

#Q-Table initialization 
Q = np.zeros((road_length, len(actions))) #Is core of Q-learning which initializes the Q-table with zeros

#Hyperparameters
episodes = 1000 
learning_rate = 0.1
gamma = 0.9 # Discount factor
epsilon = 0.1 # Exploration rate

#Training loop for agent
for episode in range(episodes):
    state = 0

    while state != 4:
        if random.uniform(0, 1) < epsilon:
            actions = random.randint(0, 1)  # Explore: choose a random action
        else: