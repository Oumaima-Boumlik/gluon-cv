"""Default setting in training/testing"""
from yacs.config import CfgNode as CN


_C = CN()

_C.DDP_CONFIG = CN(new_allowed=False)

_C.DDP_CONFIG.WORLD_SIZE = 1  # number of nodes for distributed training
_C.DDP_CONFIG.WORLD_RANK = 0  # node rank for distributed training
_C.DDP_CONFIG.GPU_WORLD_SIZE = 8
_C.DDP_CONFIG.GPU_WORLD_RANK = 0
_C.DDP_CONFIG.DIST_URL = 'tcp://127.0.0.1:10001'
_C.DDP_CONFIG.WOLRD_URLS = ['127.0.0.1']
_C.DDP_CONFIG.AUTO_RANK_MATCH = True
_C.DDP_CONFIG.DIST_BACKEND = 'nccl' # distributed backend
_C.DDP_CONFIG.GPU = 0
_C.DDP_CONFIG.DISTRIBUTED = True

###########################################################################################

_C.CONFIG = CN(new_allowed=True)

_C.CONFIG.TRAIN = CN(new_allowed=True)
_C.CONFIG.TRAIN.EPOCH_NUM = 200
_C.CONFIG.TRAIN.BATCH_SIZE = 8
_C.CONFIG.TRAIN.LR = 0.01
_C.CONFIG.TRAIN.MOMENTUM = 0.9
_C.CONFIG.TRAIN.W_DECAY = 1e-5
_C.CONFIG.TRAIN.LR_MILESTONE = [30, 60, 80]
_C.CONFIG.TRAIN.STEP = 0.1


_C.CONFIG.VAL = CN(new_allowed=True)
_C.CONFIG.VAL.FREQ = 2
_C.CONFIG.VAL.BATCH_SIZE = 8


_C.CONFIG.INFERENCE = CN(new_allowed=True)
_C.CONFIG.INFERENCE.FEAT = False


_C.CONFIG.DATA = CN(new_allowed=True)
_C.CONFIG.DATA.TRAIN_ANNO_PATH = None
_C.CONFIG.DATA.TRAIN_DATA_PATH = None
_C.CONFIG.DATA.VAL_ANNO_PATH = None
_C.CONFIG.DATA.VAL_DATA_PATH = None
_C.CONFIG.DATA.NUM_CLASSES = 400
_C.CONFIG.DATA.MULTIGRID = True
_C.CONFIG.DATA.CLIP_LEN = 32
_C.CONFIG.DATA.FRAME_RATE = 2
_C.CONFIG.DATA.KEEP_ASPECT_RATIO = False
_C.CONFIG.DATA.NUM_SEGMENT = 1
_C.CONFIG.DATA.NUM_CROP = 1
_C.CONFIG.DATA.TEST_NUM_SEGMENT = 10
_C.CONFIG.DATA.TEST_NUM_CROP = 3
_C.CONFIG.DATA.CROP_SIZE = 224
_C.CONFIG.DATA.SHORT_SIDE_SIZE = 256
_C.CONFIG.DATA.NEW_HEIGHT = 256
_C.CONFIG.DATA.NEW_WIDTH = 340


_C.CONFIG.MODEL = CN(new_allowed=True)
_C.CONFIG.MODEL.NAME = None
_C.CONFIG.MODEL.LOAD = False
_C.CONFIG.MODEL.PRETRAINED_PATH = None
_C.CONFIG.MODEL.PRETRAINED = False
_C.CONFIG.MODEL.PRETRAINED_BASE = True
_C.CONFIG.MODEL.BN_EVAL = False
_C.CONFIG.MODEL.PARTIAL_BN = False
_C.CONFIG.MODEL.BN_FROZEN = False


_C.CONFIG.LOG = CN(new_allowed=True)
_C.CONFIG.LOG.BASE_PATH = None
_C.CONFIG.LOG.EXP_NAME = 'use_time'
_C.CONFIG.LOG.LOG_DIR = 'tb_log'
_C.CONFIG.LOG.SAVE_DIR = 'checkpoints'
_C.CONFIG.LOG.SAVE_FREQ = 1
_C.CONFIG.LOG.DISPLAY_FREQ = 1
_C.CONFIG.LOG.EVAL_DIR = None


def get_cfg_defaults():
    """Get a yacs CfgNode object with default values for your project."""
    return _C.clone()
