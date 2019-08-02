<img src="https://d3000t1r8yrm6n.cloudfront.net/images/challenge_partners/image_file/35/CMU_wordmark_1500px-min.png" width="50%">  

  <img src="https://d3000t1r8yrm6n.cloudfront.net/images/challenge_partners/image_file/34/MSFT_logo_rgb_C-Gray.png" width="20%" style="margin-top:10px">


 <img src="https://raw.githubusercontent.com/AIcrowd/AIcrowd/master/app/assets/images/misc/aicrowd-horizontal.png" width="20%">   <img src="https://d3000t1r8yrm6n.cloudfront.net/images/challenge_partners/image_file/38/PFN_logo.png" width="15%" style="margin-top:10px">

# NeurIPS 2019 : MineRL Challenge Starter Kit

[![Discourse status](https://img.shields.io/discourse/https/discourse.aicrowd.com/status.svg)](https://discourse.aicrowd.com/) [![Discord](https://img.shields.io/discord/565639094860775436.svg)](https://discord.gg/BT9uegr)

Instructions to make submissions to the [NeurIPS 2019 : MineRL Challenge](https://www.aicrowd.com/challenges/neurips-2019-minerl-competition).

Participants will have to submit their code, with packaging specifications, and the evaluator will automatically build a docker image and execute their code against a series of secret datasets.

![](https://i.imgur.com/XB1WORT.gif)


### Welcome to Round 1 of the MineRL Challenge

Welcome to Round 1 everyone! This is how the competition will run! :)

1. **Sign up** to join the competition [on the AIcrowd website.](https://www.aicrowd.com/challenges/neurips-2019-minerl-competition)
2. **Clone** this repo [AIcrowd starter template](https://github.com/minerllabs/competition_submission_starter_template) and start developing your submissions.
3. **Submit** an agent to the leaderboard:
    - **Train your agents locally** (or on Azure) in under **8,000,000 samples** over **4 days**. Participants should use hardware **no more powerful than NG6v2 instances on Azure** (6 CPU cores, 112 GiB RAM, 736 GiB SDD, and a NVIDIA P100 GPU.) 
    - **Push your repository to [AIcrowd GitLab](https://gitlab.aicrowd.com)**, which verifies that it can successfully be re-trained by the organizers at the end of Round 1 and then runs the test entrypoint to evaluate the trained agent's performance! 

Once the full evaluation of the uploaded model/code is done, the participant's submission will appear on the leaderboard!

[**>> Get started now! <<** ](https://github.com/minerllabs/competition_submission_starter_template)
- [MineRL Competition Page](https://www.aicrowd.com/challenges/neurips-2019-minerl-competition) - Main registration page & leaderboard.
- [Submission Starter Template](https://github.com/minerllabs/competition_submission_starter_template) - Template for submisions and guide to submit!
- [Example Baselines](https://github.com/minerllabs/baselines) - A set of competition and non-competition baselines for `minerl`.




### Setup

- **Anaconda** (By following instructions [here](https://www.anaconda.com/download)) At least version `4.5.11` is required to correctly populate `environment.yml`.

* **Create your new conda environment**

```sh
conda create --name minerl_challenge
conda activate minerl_challenge
```

* **Your code specific dependencies**

```sh
conda install <your-package>
```

### Clone repository

```
git clone git@github.com:AIcrowd/neurips2019_minerl_challenge_starter_kit.git
cd neurips2019_minerl_challenge_starter_kit
pip install -r requirements.txt
```

### Your Submission

To get started with the environment and dataset [please check out our quick start guide here](http://minerl.io/docs/tutorials/getting_started.html)!

This competition uses a set of Gym environments based on [Malmo](https://github.com/Microsoft/malmo). The environment and dataset loader will be available through a pip package.

The main task of the competition is solving the `MineRLObtainDiamond-v0` environment. In this environment, the agent begins in a random starting location without any items, and is tasked with obtaining a diamond. This task can only be accomplished by navigating the complex item hierarchy of Minecraft.


# How do I specify my software runtime ?

The software runtime is specified by exporting your `conda` env to the root
of your repository by doing :

```
conda env export --no-build > environment.yml

# It might make sense here to remove the requirements.txt here to avoid confusion as environment.yml takes precedence over requirements.txt
```

This `environment.yml` file will be used to recreate the `conda environment`. This repository includes an example `environment.yml`

# What should my code structure be like ?

Please follow the example structure shared in the starter kit for the code structure.
The different files and directories have following meaning:

```
.
├── aicrowd.json           # Submission meta information like your username
├── apt.txt                # Packages to be installed inside docker image
├── data                   # The downloaded data, the path to directory is also available as `MINERL_DATA_ROOT` env variable
├── requirements.txt       # Python packages to be installed
├── run.sh                 # The default entry point which will execute your submission
├── test.py                # IMPORTANT: Your testing/inference phase code
├── train                  # Your trained model can be saved inside this directory
├── train.py               # IMPORTANT: Your training phase code
└── utility                # The utility scripts to provide smoother experience to you.
    ├── debug_build.sh
    ├── docker_run.sh
    ├── environ.sh
    ├── evaluation_locally.sh
    ├── parser.py
    ├── train_locally.sh
    └── verify_or_download_data.sh
```

## Important Concepts

### Repository Structure

- `aicrowd.json`
  Each repository should have a `aicrowd.json` with the following content :

```json
{
  "challenge_id": "aicrowd-neurips-2019-minerl-challenge",
  "grader_id": "aicrowd-neurips-2019-minerl-challenge",
  "authors": ["your-aicrowd-username"],
  "description": "sample description about your awesome agent",
  "license": "MIT",
  "gpu": true
}
```

This is used to map your submission to the said challenge, so please remember to use the correct `challenge_id` and `grader_id` as specified above.

Please specify if your code will a GPU or not for the evaluation of your model. If you specify `true` for the GPU, a **NVIDIA Tesla K80 GPU** will be provided and used for the evaluation.

### Packaging of your software environment

The recommended way is to use Anaconda configuration files using **environment.yml** files.

```sh
# The included environment.yml is generated by the command below, and you do not need to run it again
# if you did not add any custom dependencies

conda env export --no-build > environment.yml

# Note the `--no-build` flag, which is important if you want your anaconda env to be replicable across all
# Or if you have a rather simple softwar runtime, then even a :
#
# pip freeze > requirements.txt
#
# could work.
```

### Code Entrypoint

The evaluator will use `/home/aicrowd/run.sh` as the entrypoint, so please remember to have a `run.sh` at the root, which can instantitate any necessary environment variables, and also start executing your actual code. This repository includes a sample `run.sh` file.
If you are using a Dockerfile to specify your software environment, please remember to create a `aicrowd` user, and place the entrypoint code at `run.sh`.

The `run.sh` in turn calls your training and testing code present in `train.py` & `test.py` respectively. The inline documentation in these files will guide you in interfacing with evaluator properly.

## Dataset location

You **don't** need to upload the data set in submission and it will be provided in online submissions at `MINERL_DATA_ROOT` path. For local training and evaluations, you can download it once in your system via `./utility/verify_or_download_data.sh` or place manually into `data/` folder.

## Time constraints

### Round 1

You have to train your models locally and upload the trained model in `train/` directory. But, to make sure, your training code is compatible with further round's interface, the training code will be executed in this round as well. The constraints will be timeout of 5 minutes.

### Round 2

You are expected to train your model online using the training phase docker container and output the trained model in `train/` directory. You need to ensure that your submission is trained in under 8,000,000 samples and within 4 days period. Otherwise, the container will be killed

## Local evaluation

You can perform local training and evaluation using utility scripts shared in this directory. To mimic the online training phase you can run `./utility/train_locally.sh` from repository root, you can specify `--verbose` for complete logs.

```
aicrowd_minerl_starter_kit❯ ./utility/train_locally.sh --verbose
2019-07-22 07:58:38 root[77310] INFO Training Start...
2019-07-22 07:58:38 crowdai_api.events[77310] DEBUG Registering crowdAI API Event : CROWDAI_EVENT_INFO training_started {'event_type': 'minerl_challenge:training_started'} # with_oracle? : False
2019-07-22 07:58:40 minerl.env.malmo.instance.17c149[77310] INFO Starting Minecraft process: ['/var/folders/82/wsds_18s5dq321scc1j531m40000gn/T/tmpnyzpjrsc/Minecraft/launchClient.sh', '-port', '9001', '-env', '-runDir', '/var/folders/82/wsds_18s5dq321scc1j531m40000gn/T/tmpnyzpjrsc/Minecraft/run']
2019-07-22 07:58:40 minerl.env.malmo.instance.17c149[77310] INFO Starting process watcher for process 77322 @ localhost:9001
2019-07-22 07:58:48 minerl.env.malmo.instance.17c149[77310] DEBUG This mapping 'snapshot_20161220' was designed for MC 1.11! Use at your own peril.
2019-07-22 07:58:48 minerl.env.malmo.instance.17c149[77310] DEBUG #################################################
2019-07-22 07:58:48 minerl.env.malmo.instance.17c149[77310] DEBUG          ForgeGradle 2.2-SNAPSHOT-3966cea
2019-07-22 07:58:48 minerl.env.malmo.instance.17c149[77310] DEBUG   https://github.com/MinecraftForge/ForgeGradle
2019-07-22 07:58:48 minerl.env.malmo.instance.17c149[77310] DEBUG #################################################
2019-07-22 07:58:48 minerl.env.malmo.instance.17c149[77310] DEBUG                Powered by MCP unknown
2019-07-22 07:58:48 minerl.env.malmo.instance.17c149[77310] DEBUG              http://modcoderpack.com
2019-07-22 07:58:48 minerl.env.malmo.instance.17c149[77310] DEBUG          by: Searge, ProfMobius, Fesh0r,
2019-07-22 07:58:48 minerl.env.malmo.instance.17c149[77310] DEBUG          R4wk, ZeuX, IngisKahn, bspkrs
2019-07-22 07:58:48 minerl.env.malmo.instance.17c149[77310] DEBUG #################################################
2019-07-22 07:58:48 minerl.env.malmo.instance.17c149[77310] DEBUG Found AccessTransformer: malmomod_at.cfg
2019-07-22 07:58:49 minerl.env.malmo.instance.17c149[77310] DEBUG :deobfCompileDummyTask
2019-07-22 07:58:49 minerl.env.malmo.instance.17c149[77310] DEBUG :deobfProvidedDummyTask
...
```

For local evaluation of your code, you can use `./utility/evaluation_locally.sh`, add `--verbose` if you want to view complete logs.

```
aicrowd_minerl_starter_kit❯ ./utility/evaluation_locally.sh
{'state': 'RUNNING', 'score': {'score': 0.0, 'score_secondary': 0.0}, 'instances': {'1': {'totalNumberSteps': 1001, 'totalNumberEpisodes': 0, 'currentEnvironment': 'MineRLObtainDiamond-v0', 'state': 'IN_PROGRESS', 'episodes': [{'numTicks': 1001, 'environment': 'MineRLObtainDiamond-v0', 'rewards': 0.0, 'state': 'IN_PROGRESS'}], 'score': {'score': 0.0, 'score_secondary': 0.0}}}}
{'state': 'RUNNING', 'score': {'score': 0.0, 'score_secondary': 0.0}, 'instances': {'1': {'totalNumberSteps': 2001, 'totalNumberEpisodes': 0, 'currentEnvironment': 'MineRLObtainDiamond-v0', 'state': 'IN_PROGRESS', 'episodes': [{'numTicks': 2001, 'environment': 'MineRLObtainDiamond-v0', 'rewards': 0.0, 'state': 'IN_PROGRESS'}], 'score': {'score': 0.0, 'score_secondary': 0.0}}}}
{'state': 'RUNNING', 'score': {'score': 0.0, 'score_secondary': 0.0}, 'instances': {'1': {'totalNumberSteps': 3001, 'totalNumberEpisodes': 0, 'currentEnvironment': 'MineRLObtainDiamond-v0', 'state': 'IN_PROGRESS', 'episodes': [{'numTicks': 3001, 'environment': 'MineRLObtainDiamond-v0', 'rewards': 0.0, 'state': 'IN_PROGRESS'}], 'score': {'score': 0.0, 'score_secondary': 0.0}}}}
{'state': 'RUNNING', 'score': {'score': 0.0, 'score_secondary': 0.0}, 'instances': {'1': {'totalNumberSteps': 4001, 'totalNumberEpisodes': 0, 'currentEnvironment': 'MineRLObtainDiamond-v0', 'state': 'IN_PROGRESS', 'episodes': [{'numTicks': 4001, 'environment': 'MineRLObtainDiamond-v0', 'rewards': 0.0, 'state': 'IN_PROGRESS'}], 'score': {'score': 0.0, 'score_secondary': 0.0}}}}
{'state': 'RUNNING', 'score': {'score': 0.0, 'score_secondary': 0.0}, 'instances': {'1': {'totalNumberSteps': 5001, 'totalNumberEpisodes': 0, 'currentEnvironment': 'MineRLObtainDiamond-v0', 'state': 'IN_PROGRESS', 'episodes': [{'numTicks': 5001, 'environment': 'MineRLObtainDiamond-v0', 'rewards': 0.0, 'state': 'IN_PROGRESS'}], 'score': {'score': 0.0, 'score_secondary': 0.0}}}}
{'state': 'RUNNING', 'score': {'score': 0.0, 'score_secondary': 0.0}, 'instances': {'1': {'totalNumberSteps': 6001, 'totalNumberEpisodes': 0, 'currentEnvironment': 'MineRLObtainDiamond-v0', 'state': 'IN_PROGRESS', 'episodes': [{'numTicks': 6001, 'environment': 'MineRLObtainDiamond-v0', 'rewards': 0.0, 'state': 'IN_PROGRESS'}], 'score': {'score': 0.0, 'score_secondary': 0.0}}}}
...
```

The steps to mimic above in a docker environment will be added shortly.

## Submission

To make a submission, you will have to create a private repository on [https://gitlab.aicrowd.com/](https://gitlab.aicrowd.com/).

You will have to add your SSH Keys to your GitLab account by following the instructions [here](https://docs.gitlab.com/ee/gitlab-basics/create-your-ssh-keys.html).
If you do not have SSH Keys, you will first need to [generate one](https://docs.gitlab.com/ee/ssh/README.html#generating-a-new-ssh-key-pair).

Then you can create a submission by making a _tag push_ to your repository on [https://gitlab.aicrowd.com/](https://gitlab.aicrowd.com/).
**Any tag push (where the tag name begins with "submission-") to your private repository is considered as a submission**  
Then you can add the correct git remote, and finally submit by doing :

```
cd neurips2019_minerl_challenge_starter_kit
# Add AIcrowd git remote endpoint
git remote add aicrowd git@gitlab.aicrowd.com:<YOUR_AICROWD_USER_NAME>/neurips2019_minerl_challenge_starter_kit.git
git push aicrowd master

# Create a tag for your submission and push
git tag -am "submission-v0.1" submission-v0.1
git push aicrowd master
git push aicrowd submission-v0.1

# Note : If the contents of your repository (latest commit hash) does not change,
# then pushing a new tag will **not** trigger a new evaluation.
```

You now should be able to see the details of your submission at :
[gitlab.aicrowd.com/<YOUR_AICROWD_USER_NAME>/neurips2019_minerl_challenge_starter_kit/issues](gitlab.aicrowd.com//<YOUR_AICROWD_USER_NAME>/neurips2019_minerl_challenge_starter_kit/issues)

**NOTE**: Remember to update your username in the link above :wink:

In the link above, you should start seeing something like this take shape (each of the steps can take a bit of time, so please be patient too :wink: ) :
![](https://i.imgur.com/FqScw4m.png)

and if everything works out correctly, then you should be able to see the final scores like this :
![](https://i.imgur.com/u00qcif.png)

**Best of Luck** :tada: :tada:

# Author

Shivam Khandelwal <https://twitter.com/skbly7>
