import aicrowd_helper
import train
import test

import os
EVALUATION_RUNNING_ON = os.getenv('EVALUATION_RUNNING_ON', None)
EVALUATION_STAGE = os.getenv('EVALUATION_STAGE', 'all')
EXITED_SIGNAL_PATH = os.getenv('EXITED_SIGNAL_PATH', 'shared/exited')

# Training Phase
if EVALUATION_STAGE in ['all', 'training']:
    aicrowd_helper.training_start()
    train.main()
    try:
        train.main()
        aicrowd_helper.training_end()
    except Exception as e:
        aicrowd_helper.training_error()
        print(e)


# Testing Phase
if EVALUATION_STAGE in ['all', 'testing']:
    if EVALUATION_RUNNING_ON in ['local']:
        os.remove(EXITED_SIGNAL_PATH)
    aicrowd_helper.inference_start()
    try:
        test.main()
        aicrowd_helper.inference_end()
    except Exception as e:
        aicrowd_helper.inference_error()
        print(e)
    if EVALUATION_RUNNING_ON in ['local']:
        from pathlib import Path
        Path(EXITED_SIGNAL_PATH).touch()

# Launch instance manager
if EVALUATION_STAGE in ['manager']:
    from minerl.env.malmo import launch_instance_manager
    launch_instance_manager()