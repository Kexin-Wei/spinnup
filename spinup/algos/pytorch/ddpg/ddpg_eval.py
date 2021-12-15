import spinup.algos.pytorch.ddpg.core as core
import torch
import sys
sys.path.append('.')
print(sys.path)


if __name__ == '__main__':
    import argparse
    import os
    from env_pyrep.env_laparo_aty import Laparo_Sim_artery
    from env_pyrep.EvaluateDisplay import human_evaluate

    parser = argparse.ArgumentParser()
    parser.add_argument('--hid', type=int, default=256)
    parser.add_argument('--l', type=int, default=2)
    parser.add_argument('--num_test_episodes', type=int, default=10)
    parser.add_argument('--random_start', action='store_false')
    args = parser.parse_args()

    ac_kwargs=dict(hidden_sizes=[args.hid]*args.l)
    actor_critic=core.MLPActorCritic
    env1 = Laparo_Sim_artery(bounded=True,headless=True,random_start=args.random_start)
    env2 = Laparo_Sim_artery(bounded=True,headless=False,random_start=args.random_start)

    ac = actor_critic(env1.observation_space, env1.action_space, **ac_kwargs)    
    intel_path = '2021-12-11_ddpg/2021-12-11_15-18-42-ddpg_s0'

    ac = torch.load(os.path.join("output",intel_path,"pyt_save/model.pt"))

    human_evaluate(ac,env1,env2,epochs=1)
