from sample_factory.launcher.run_description import RunDescription, Experiment, ParamGrid
from swarm_rl.runs.quad_multi_mix_baseline import QUAD_BASELINE_CLI

_params = ParamGrid([
    ('seed', [0000, 1111, 2222, 3333]),
])

_experiment_no_replay = Experiment(
    'quad_mix_baseline-8_mixed_noreplay',
    QUAD_BASELINE_CLI + ' --replay_buffer_sample_prob=0.00',
    _params.generate_params(randomize=False),
)

_experiment_no_anneal = Experiment(
    'quad_mix_baseline-8_mixed_noannealing',
    QUAD_BASELINE_CLI + ' --anneal_collision_steps=0',
    _params.generate_params(randomize=False),
)

RUN_DESCRIPTION = RunDescription('paper_quads_multi_mix_baseline_8a_ablation_v116', experiments=[_experiment_no_replay, _experiment_no_anneal])

# On Brain server, when you use num_workers = 72, if the system reports: Resource temporarily unavailable,
# then, try to use two commands below
# export OMP_NUM_THREADS=1
# export USE_SIMPLE_THREADED_LEVEL3=1

# Command to use this script on server:
# xvfb-run python -m launcher.run --run=quad_multi_mix_baseline --runner=processes --max_parallel=3 --pause_between=1 --experiments_per_gpu=1 --num_gpus=3
# Command to use this script on local machine:
# Please change num_workers to the physical cores of your local machine
# python -m launcher.run --run=quad_multi_mix_baseline --runner=processes --max_parallel=3 --pause_between=1 --experiments_per_gpu=1 --num_gpus=3
