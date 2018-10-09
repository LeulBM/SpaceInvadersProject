import argparse
import sys
#import pdb
import gym
from gym import wrappers, logger
import random

class Agent(object):
    """The Twitch Shooter"""
    def __init__(self, action_space):
        self.action_space = action_space

    # You should modify this function
    def act(self, observation, reward, done):
        # Dict of all color values
        colorvalues = {
                80: "Ground",
                162: "Yellow Text",
                0: "Background",
                142: "Bullet",  #
                181: "Blockers",#
                50: "Ship",
                134: "Alien"}   #

        # Find ship
        ship = -1
        for x in range(0, 160):
            if observation[185][x][0] == 50:
                ship = x
                break

        # Return 0 if ship isn't found to try and force ship to spawn
        if ship == -1:
            return 0

        searchleft = ship-5
        searchright = ship+5

        # Search column directly above ship
        while searchleft > 34 and searchright < 123:
            for y in range(184, 0, -1):
                for x in range(searchleft, searchright):
                    redpix = observation[y][x][0]
                    objfound = colorvalues.get(redpix)

                    if objfound == "Bullet":
                        if x > ship:
                            return 5
                        else:
                            return 4
                    elif objfound == "Alien":
                        if x > ship:
                            return 4
                        else:
                            return 5
            searchleft -= 10
            searchright += 10

        if(searchleft <= 34):
            return 4
        else:
            return 4

## YOU MAY NOT MODIFY ANYTHING BELOW THIS LINE OR USE
## ANOTHER MAIN PROGRAM
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('env_id', nargs='?', default='SpaceInvaders-v0', help='Select the environment to run')
    args = parser.parse_args()

    # You can set the level to logger.DEBUG or logger.WARN if you
    # want to change the amount of output.
    logger.set_level(logger.INFO)

    env = gym.make(args.env_id)

    # You provide the directory to write to (can be an existing
    # directory, including one with existing data -- all monitor files
    # will be namespaced). You can also dump to a tempdir if you'd
    # like: tempfile.mkdtemp().
    outdir = 'random-agent-results'


    env.seed(0)
    agent = Agent(env.action_space)

    episode_count = 100
    reward = 0
    done = False
    score = 0
    special_data = {}
    special_data['ale.lives'] = 3
    ob = env.reset()
    while not done:
        
        action = agent.act(ob, reward, done)
        ob, reward, done, _ = env.step(action)
        score += reward
        env.render()
     
    # Close the env and write monitor result info to disk
    print ("Your score: %d" % score)
    env.close()
