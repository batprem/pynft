# Requirements

## Python


```python
import sys


python_version = (
    f"{sys.version_info.major}."
    f"{sys.version_info.minor}."
    f"{sys.version_info.micro}"
)
print(f"Python version {python_version}")
```

    Python version 3.8.12


Choose any following methods to install dependcies
* poetry (recommend) <br/><br/>
 `poetry install` <br/><br/>
* pip <br/><br/>
`pip install -r requirements.txt`

## IPFS CLI

Follow this URL https://docs.ipfs.io/install/command-line/#official-distributions

# Import modules


```python
import brownie
from brownie import accounts, project, config, network

# Compile smart contracts
p = project.load('.', name="pynft")
p.load_config()
```

# Connect to chain


```python
import os

print("Available networks")
print(os.popen("brownie networks list").read())
```

    Available networks
    Brownie v1.17.0 - Python development framework for Ethereum
    
    The following networks are declared:
    
    Ethereum
    [0;1;30m  ├─[0;mMainnet (Infura): [0;32mmainnet[0;m
    [0;1;30m  ├─[0;mRopsten (Infura): [0;32mropsten[0;m
    [0;1;30m  ├─[0;mRinkeby (Infura): [0;32mrinkeby[0;m
    [0;1;30m  ├─[0;mGoerli (Infura): [0;32mgoerli[0;m
    [0;1;30m  ├─[0;mKovan (Infura): [0;32mkovan[0;m
    [0;1;30m  ├─[0;mmainnet-fork-2: [0;32mmainnet-fork-2[0;m
    [0;1;30m  ├─[0;mmainnet-fork-3: [0;32mmainnet-fork-3[0;m
    [0;1;30m  ├─[0;mmainnet-fork-4: [0;32mmainnet-fork-4[0;m
    [0;1;30m  └─[0;mmainnet-fork-5: [0;32mmainnet-fork-5[0;m
    
    Ethereum Classic
    [0;1;30m  ├─[0;mMainnet: [0;32metc[0;m
    [0;1;30m  └─[0;mKotti: [0;32mkotti[0;m
    
    Arbitrum
    [0;1;30m  └─[0;mMainnet: [0;32marbitrum-main[0;m
    
    Binance Smart Chain
    [0;1;30m  ├─[0;mTestnet: [0;32mbsc-test[0;m
    [0;1;30m  └─[0;mMainnet: [0;32mbsc-main[0;m
    
    Fantom Opera
    [0;1;30m  ├─[0;mTestnet: [0;32mftm-test[0;m
    [0;1;30m  └─[0;mMainnet: [0;32mftm-main[0;m
    
    Harmony
    [0;1;30m  └─[0;mMainnet (Shard 0): [0;32mharmony-main[0;m
    
    Polygon
    [0;1;30m  ├─[0;mMainnet (Infura): [0;32mpolygon-main[0;m
    [0;1;30m  └─[0;mMumbai Testnet (Infura): [0;32mpolygon-test[0;m
    
    XDai
    [0;1;30m  ├─[0;mMainnet: [0;32mxdai-main[0;m
    [0;1;30m  └─[0;mTestnet: [0;32mxdai-test[0;m
    
    Eherium
    [0;1;30m  └─[0;mganache-local: [0;32mganache-local[0;m
    
    Etherium
    [0;1;30m  └─[0;mganache-local-2: [0;32mganache-local-2[0;m
    
    cronos
    [0;1;30m  └─[0;mcronos-testnet: [0;32mcronos-testnet[0;m
    
    Development
    [0;1;30m  ├─[0;mGanache-CLI: [0;32mdevelopment[0;m
    [0;1;30m  ├─[0;mGeth Dev: [0;32mgeth-dev[0;m
    [0;1;30m  ├─[0;mHardhat: [0;32mhardhat[0;m
    [0;1;30m  ├─[0;mHardhat (Mainnet Fork): [0;32mhardhat-fork[0;m
    [0;1;30m  ├─[0;mGanache-CLI (Mainnet Fork): [0;32mmainnet-fork[0;m
    [0;1;30m  ├─[0;mGanache-CLI (BSC-Mainnet Fork): [0;32mbsc-main-fork[0;m
    [0;1;30m  ├─[0;mGanache-CLI (FTM-Mainnet Fork): [0;32mftm-main-fork[0;m
    [0;1;30m  ├─[0;mGanache-CLI (Polygon-Mainnet Fork): [0;32mpolygon-main-fork[0;m
    [0;1;30m  ├─[0;mGanache-CLI (XDai-Mainnet Fork): [0;32mxdai-main-fork[0;m
    [0;1;30m  ├─[0;mlocal: [0;32mlocal[0;m
    [0;1;30m  ├─[0;mmainnet-fork-dev: [0;32mmainnet-fork-dev[0;m
    [0;1;30m  └─[0;mcronos-mainnet-fork: [0;32mcronos-mainnet-fork[0;m
    


## Connect


```python
NETWORK = "rinkeby"
# network.connect(NETWORK) # Main net fork
# network.connect(NETWORK) # Main net
network.connect(NETWORK) # Test net rinkeby
```

# Account


```python
!brownie accounts list
```

    Brownie v1.17.0 - Python development framework for Ethereum
    
    Found 4 accounts:
     [0;1;30m├─[0;1;34meth-main[0;m: [0;1;35m0xf6EfbD8142A18E741360b41301eDFdbD2719D03C[0;m
     [0;1;30m├─[0;1;34mprem[0;m: [0;1;35m0xedEa45C169753E1af9bf1cb1c374Ca83EBd0d6BE[0;m
     [0;1;30m├─[0;1;34mtest[0;m: [0;1;35m0xA3c11aDE2244474EB2F8167921216AB6541F9bA8[0;m
     [0;1;30m└─[0;1;34mtest_2[0;m: [0;1;35m0xA3c11aDE2244474EB2F8167921216AB6541F9bA8[0;m



```python
if NETWORK == "mainnet" and False:
    from scripts.helpful_script import get_account

    account = get_account()

else:
    from brownie import accounts

    accounts.load("eth-main") # Main net
    account = accounts[0]

```

    Enter password for "eth-main": ········



```python
print(account)
```

    0xf6EfbD8142A18E741360b41301eDFdbD2719D03C


# Dump variables


```python
for key, value in p.__dict__.items():
    print(key)
    brownie.__dict__[key] = p.__dict__[key]
```

    _path
    _envvars
    _structure
    _build_path
    _name
    _active
    _sources
    _build
    _compiler_config
    interface
    _containers
    PYNFT
    ERC721
    Strings
    __all__
    _namespaces


# Deploy contracts


```python
from brownie import PYNFT


pynft = PYNFT.deploy({"from": account})
```

    Transaction sent: [0;1;34m0xa2a16103b7ce13a0015421ea2cfdbb3319f6617d16e65c6175a50ea57a09bfab[0;m
      Gas price: [0;1;34m1.705944452[0;m gwei   Gas limit: [0;1;34m1419476[0;m   Nonce: [0;1;34m29[0;m
      PYNFT.constructor confirmed   Block: [0;1;34m10057857[0;m   Gas used: [0;1;34m1290433[0;m ([0;1;34m90.91%[0;m)
      PYNFT deployed at: [0;1;34m0xeee906fAE06C0456b57A11cBd5Cec4628fBDAAf2[0;m
    


# Upload file to IPFS

## Assets


```python
prefix = "assets/"


def upload_to_ipfs(filepath: str) -> str:
    return os.popen(f"ipfs add -q {filepath}").read().strip()

def is_an_image(filename: str):
    """
    Description:
        Check if a file is an image
    paramgs:
        filename:
            (str) filename, should be with its extension
    returns:
        (str) qid of ipfs
    """
    for extention in [".png", "jpg"]:
        if filename.endswith(extention):
            return True
    return False

def set_ipfs_share_link(prefix: str, asset: str) -> str:
    """
    description:
        Run IPFS upload process and return share link URL
    params:
        prefix:
            (str) Local prefix file
        asset:
            (str) Filename
    returns:
        (str) share link url
    """
    IPFS_PREFIX = "https://ipfs.io/ipfs"
    qid = upload_to_ipfs(f"{prefix}{asset}".replace(" ", "\ "))
    asset = asset.replace(" ", "-")
    return f"{IPFS_PREFIX}/{qid}?filename={asset}"



class Attribute:
    pass


attribute = Attribute()
for asset in os.listdir(prefix):
    if asset.startswith(".") or asset == "metadata.json":
        # Skip
        continue
    ipfs_share_link = set_ipfs_share_link(prefix, asset)
    if is_an_image(asset):
        setattr(attribute, "image_url", ipfs_share_link)
    else:
        setattr(attribute, "external_url", ipfs_share_link)
    print(ipfs_share_link)
```

    https://ipfs.io/ipfs/Qmda8x41dArU36LKveHzSN3NPJjWxFgyeNNLM8uUMqtMNr?filename=my-first-python-code.png
    https://ipfs.io/ipfs/QmUoGY6GbvzSQi2gP7YHtVMRocNW1Xs16ZUHxWcTgWHwJb?filename=fruit-list.py


# Set up metadata

## Render metadata from template


```python
metadata = {
    "description": """It was in 2015, I was an engineer intern.
    
I was assigned to code in Python for satellite signal processing.

At that time, I had no experience with it, but I had completed C#, C and Matlab courses.

It inspired me to transfer from electrical to software engineer career path.

Now, I partially succeed in software engineering, machine learning and A.I implementation.

This NFT determines where I started.

Moreover, I minting this NFT with my Solidity code I created by myself.

No, it's not my first Solidity project :D

But it's my first Solidity project deployed in `production`.

Which means this is the starting point for my smart contract development.

Smart contract repository is located in https://github.com/batprem/pynft
""", 
    "external_url": attribute.external_url, 
    "image": attribute.image_url, 
    "name": "My first Python code",
    "attributes": [], 
}
```

## Save metadata into JSON


```python
import json


metadata_filename = "metadata.json"

with open(f"assets/{metadata_filename}", "w") as json_file:
    json.dump(metadata, json_file)
    
metadata_share_link = set_ipfs_share_link(prefix, metadata_filename)
```

# Assign to smart contract

## Mint


```python
PYNFT[-1].createCollectable({"from": account}).wait(1)
```

    Transaction sent: [0;1;34m0xce49cf20c4a9a7b70408ef8ccd9449ef6001c7a300f679af65d29cee4fe851f2[0;m
      Gas price: [0;1;34m1.721482323[0;m gwei   Gas limit: [0;1;34m102072[0;m   Nonce: [0;1;34m30[0;m
      PYNFT.createCollectable confirmed   Block: [0;1;34m10057863[0;m   Gas used: [0;1;34m92793[0;m ([0;1;34m90.91%[0;m)
    
      PYNFT.createCollectable confirmed   Block: [0;1;34m10057863[0;m   Gas used: [0;1;34m92793[0;m ([0;1;34m90.91%[0;m)
    


## Set URI


```python
PYNFT[-1].setBaseURI(metadata_share_link, {"from": account}).wait(1)
```

    Transaction sent: [0;1;34m0x516f50b0b592ffbfe76dbc4a91595b16bc96c40be05491444d2eeb0c8a954321[0;m
      Gas price: [0;1;34m1.653401301[0;m gwei   Gas limit: [0;1;34m38577[0;m   Nonce: [0;1;34m32[0;m
      PYNFT.setBaseURI confirmed   Block: [0;1;34m10057867[0;m   Gas used: [0;1;34m35070[0;m ([0;1;34m90.91%[0;m)
    
      PYNFT.setBaseURI confirmed   Block: [0;1;34m10057867[0;m   Gas used: [0;1;34m35070[0;m ([0;1;34m90.91%[0;m)
    



```python
PYNFT[-1].tokenURI(0)
```




    'https://ipfs.io/ipfs/QmQBZ6VjMeDphzuTGQxxSst7565yjgwvvs8GHtwbayw6hU?filename=metadata.json'




```python
PYNFT[-1].tokenCounter()
```




    1



## Reference

* https://www.youtube.com/watch?v=M576WGiDBdQ&t=8373s
