import warnings

warnings.warn(
    "swarm-lm-node.dht_utils has been moved to swarm-lm-node.utils.dht. This alias will be removed in Petals 2.2.0+",
    DeprecationWarning,
    stacklevel=2,
)

from .utils.dht import *
