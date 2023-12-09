import torch

PUBLIC_INITIAL_PEERS = [
   "/ip4/130.250.185.236/tcp/32722/p2p/12D3KooWP5r4eTKjBoYa23FrGHmkpYHZZFW5y6dEJt4Qyd5ykPjQ"
]

# The reachability API is currently used only when connecting to the public swarm
REACHABILITY_API_URL = "https://health.swarmlm.xyz"

DTYPE_MAP = dict(bfloat16=torch.bfloat16, float16=torch.float16, float32=torch.float32, auto="auto")
