import torch

PUBLIC_INITIAL_PEERS = [
    "'/ip4/146.190.171.104/tcp/45481/p2p/12D3KooWAcx7je3wqkS6mnJVkcRYLd1hpmfPbz3wZqb1b1Py2rXU'"
]

# The reachability API is currently used only when connecting to the public swarm
REACHABILITY_API_URL = "https://health.swarmlm.xyz"

DTYPE_MAP = dict(bfloat16=torch.bfloat16, float16=torch.float16, float32=torch.float32, auto="auto")
